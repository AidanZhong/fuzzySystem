import random

import Case2


def generate_random_interval(min_val, max_val, max_width):
    """
    Generate a random interval within [min_val, max_val] with a maximum width.
    """
    start = random.uniform(min_val, max_val - max_width)
    end = start + random.uniform(0, max_width)
    return (start, min(end, max_val))  # Ensure the interval does not exceed max_val


def generate_test_pairs(num_pairs, max_width=5):
    """
    Generate test input pairs where each pair differs in only one variable.
    :param num_pairs: Number of test pairs to generate.
    :param max_width: Maximum width for the random intervals.
    :return: List of test pairs.
    """
    # Linguistic term ranges
    temperature_range = (24, 44)  # Temperature range
    headache_range = (0, 10)  # Headache range
    age_range = (0, 130)  # Age range

    pairs = []

    for _ in range(num_pairs):
        # Generate a random input
        temp_interval = generate_random_interval(*temperature_range, max_width)
        headache_interval = generate_random_interval(*headache_range, max_width)
        age_interval = generate_random_interval(*age_range, max_width)

        # Randomly choose a control variable to change
        control_var = random.choice(["temperature", "headache", "age"])

        if control_var == "temperature":
            # Change temperature while keeping others the same
            new_temp_interval = generate_random_interval(*temperature_range, max_width)
            pairs.append(((temp_interval, headache_interval, age_interval),
                          (new_temp_interval, headache_interval, age_interval)))

        elif control_var == "headache":
            # Change headache while keeping others the same
            new_headache_interval = generate_random_interval(*headache_range, max_width)
            pairs.append(((temp_interval, headache_interval, age_interval),
                          (temp_interval, new_headache_interval, age_interval)))

        elif control_var == "age":
            # Change age while keeping others the same
            new_age_interval = generate_random_interval(*age_range, max_width)
            pairs.append(((temp_interval, headache_interval, age_interval),
                          (temp_interval, headache_interval, new_age_interval)))

    return pairs


# Example Usage
if __name__ == "__main__":
    num_pairs = 30  # Generate 10 pairs
    test_pairs = generate_test_pairs(num_pairs)
    case = Case2.Case2()

    for i, (input1, input2) in enumerate(test_pairs, 1):
        print(f"Pair {i}:")
        print(f"  Input 1: Temperature={input1[0]}, Headache={input1[1]}, Age={input1[2]}")
        print(f"  Input 2: Temperature={input2[0]}, Headache={input2[1]}, Age={input2[2]}")

        res1 = case.Result_for_interval_using_fixed_step(case.Result_with_centroid_type_reduction, input1[0], input1[1],
                                                        input1[2],
                                                        total_steps_for_each_var=5)
        print(f"Temperature:{input1[0]}, Headache:{input1[1]}, Age:{input1[2]}, result: {res1}")

        res2 = case.Result_for_interval_using_fixed_step(case.Result_with_centroid_type_reduction, input2[0], input2[1],
                                                        input2[2],
                                                        total_steps_for_each_var=5)
        print(f"Temperature:{input2[0]}, Headache:{input2[1]}, Age:{input2[2]}, result: {res2}")


