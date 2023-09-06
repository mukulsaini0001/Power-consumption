import psutil
import time

def measure_power_consumption(application_name, duration_seconds):
    pid = None
    for process in psutil.process_iter(attrs=['pid', 'name']):
        if process.info['name'] == application_name:
            pid = process.info['pid']
            break

    if pid is None:
        print(f"Application '{application_name}' not found.")
        return

    before_cpu_usage = psutil.cpu_percent()
    before_memory_usage = psutil.virtual_memory().percent
    start_time = time.time()
    while time.time() - start_time < duration_seconds:
        if not psutil.pid_exists(pid):
            break
        time.sleep(1)

    after_cpu_usage = psutil.cpu_percent()
    after_memory_usage = psutil.virtual_memory().percent

    delta_cpu = after_cpu_usage - before_cpu_usage
    delta_memory = after_memory_usage - before_memory_usage

    print(f"Estimated power consumption of '{application_name}':")
    print(f"CPU Usage: {delta_cpu}%")
    print(f"Memory Usage: {delta_memory}%")


if __name__ == "__main__":
    target_applications = input("Enter target applications: ").split(',')
    measurement_duration_seconds = int(input("Enter measurement duration in seconds: "))
    target_applications = [app.strip() for app in target_applications]  

    
    for app_name in target_applications:
        app_name = app_name.strip()  
        measure_power_consumption(app_name, measurement_duration_seconds) 




    

