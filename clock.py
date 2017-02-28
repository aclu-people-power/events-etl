from apscheduler.schedulers.blocking import BlockingScheduler
from etl.indivisible import main as indivisible
from etl.peoplepower import main as peoplepower


sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=60)
def timed_job():
    print('This job is run every minute')
    try:
        indivisible.run()
        peoplepower.run()
    except ValueError as error:
        print('Caught this error: ' + repr(error))

    
sched.start()
