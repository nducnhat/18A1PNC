import threading

def giai_thua(start, end, result):
    partial_result = 1
    for i in range(start, end + 1):
        partial_result *= i
    result.append(partial_result)

def tinh_giai_thua(number, num_threads):
    result = []
    threads = []
    step = number // num_threads
    start = 1
    end = step

    for _ in range(num_threads):
        thread = threading.Thread(target=giai_thua, args=(start, end, result))
        threads.append(thread)
        thread.start()

        start = end + 1
        end = start + step - 1 if end + step <= number else number

    for thread in threads:
        thread.join()

    final_result = 1
    for partial_result in result:
        final_result *= partial_result

    return final_result

if __name__ == "__main__":
    number_to_factorial = 5
    num_threads = 2

    result = tinh_giai_thua(number_to_factorial, num_threads)
    print(f"Giai thừa của {number_to_factorial} là {result}")
