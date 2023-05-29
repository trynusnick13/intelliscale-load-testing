import concurrent.futures
import os
import time

import requests
import typer

BASE_URL = os.getenv("BASE_URL", "http://localhost")

app = typer.Typer()

@app.command()
def run_stress_load_campaign(requests_count: int):
    print("Running stress load campaign")
    start = time.time()
    destination_url = f"{BASE_URL}/matrix/{100}"
    for _ in range(requests_count):
        response = requests.get(destination_url)
        print(response.text)
    print(f"Total execution time: {time.time() - start}")


@app.command()
def run_parallel_stress_load_campaign(requests_count: int):
    print("Running stress load campaign")
    start = time.time()
    destination_url = f"{BASE_URL}/matrix/{100}"
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for _ in range(requests_count):
            futures.append(executor.submit(requests.get, url=destination_url))
        for future in concurrent.futures.as_completed(futures):
            print(future.result().text)
    print(f"Total execution time: {time.time() - start}")


@app.command()
def ping():
    print("Pong")

if __name__ == "__main__":
    app()
