def power_digit_sum(num,power):
    power_sum = num**power
    print(power_sum)
    sum_digit = 0
    for i in str(power_sum):
        sum_digit+=int(i)
    print(sum_digit)


if __name__ == "__main__":
    power_digit_sum(2,1000)
