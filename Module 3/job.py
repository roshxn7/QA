from pyats.easypy import Task

def main(runtime):
    # Specify the path to your test script
    test_script = 'ap_test.py'
    
    # Create a Task
    task = Task(testscript=test_script)
    
    # Run the Task
    task.run()