from Foundation import NSRunLoop, NSDate # type: ignore 
from EventKit import EKEventStore, EKEntityTypeReminder  # type: ignore
from datetime import date

def retrieve_reminders(TARGET_LIST="TO DO"):
    store = EKEventStore.alloc().init()
    granted = False
    done = False

    def access_handler(_granted, _error):
        nonlocal granted, done
        granted = _granted
        done = True

    def clear_completed_reminders(reminders):
        for r in reminders:
            if r.isCompleted():
                store.removeReminder_commit_error_(r, True, None)
        

    store.requestAccessToEntityType_completion_(
        EKEntityTypeReminder,
        access_handler
    )

    while not done:
        NSRunLoop.currentRunLoop().runUntilDate_(
            NSDate.dateWithTimeIntervalSinceNow_(0.1)
        )

    if not granted:
        raise SystemExit("Reminders access denied")

    calendar = None
    for cal in store.calendarsForEntityType_(EKEntityTypeReminder):
        if cal.title() == TARGET_LIST:
            calendar = cal
            break

    if not calendar:
        raise SystemExit(f"List '{TARGET_LIST}' not found")

    predicate = store.predicateForRemindersInCalendars_([calendar])

    done = False
    reminders = []

    def fetch_handler(_reminders):
        nonlocal reminders, done
        reminders = _reminders or []
        done = True

    store.fetchRemindersMatchingPredicate_completion_(
        predicate,
        fetch_handler
    )

    while not done:
        NSRunLoop.currentRunLoop().runUntilDate_(
            NSDate.dateWithTimeIntervalSinceNow_(0.1)
        )


    reminders_list = []
    for r in reminders:
        title = r.title()
        completed = r.isCompleted()
        due = r.dueDateComponents()
        if due and due.year() and due.month() and due.day():
            due_date = date(due.year(), due.month(), due.day())
            if due_date > date.today():
                continue  # Skip future reminders
        due_str = (
            f"{due.year()}-{due.month():02d}-{due.day():02d}"
            if due else "None"
        )
        reminders_list.append(f"{title} | Completed: {completed} | Due: {due_str}")

    clear_completed_reminders(reminders)
    return "\n".join(reminders_list)