import numpy as np
import matplotlib.pyplot as plt

def main():
    h3 = np.genfromtxt(
    r"C:\Users\elgen\Downloads\MECE_Lab1_Data - Sheet1.csv",
    delimiter=",",
    skip_header=1,
    usecols=(1),
    dtype=None,
    encoding="utf-8-sig"
    )

    h0 = 150            # 150 cm
    sum = 0
    length = len(h3)
    e = np.zeros(length)

    # Calculates the sum of all data points to calculate the mean
    for i in range(length):
        sum = sum+ h3[i]
        e[i] = (h3[i]/h0)** 0.5
    
    mean = sum/length
    print("Mean:", mean)

    sumdis = 0
    esumdis = 0
    for i in range(length):
        distomean = (h3[i] - mean) ** 2
        sumdis = sumdis + distomean

        edistomean = (e[i] - np.mean(e)) ** 2
        esumdis = esumdis + edistomean
        
    print("e:", e)

    variance = sumdis/length
    stddev = variance ** 0.5
    
    print("Variance:", variance)
    print("Standard Deviation:", stddev)

    coeff_of_restitution = np.mean(e)
    evariance = esumdis/length
    estddev = evariance ** 0.5

    print("Coefficient of Restitution:", coeff_of_restitution)
    print("e Variance:", evariance)
    print("e Standard Deviation:", estddev)

    # Plot histogram for rebound heights
    plt.hist(h3, bins=10, edgecolor='black', color='skyblue')

    # edges: centers the bins for the histogram based on the rebound heights
    edges = np.histogram_bin_edges(h3, bins=10)
    print("Histogram edges:", edges)
    # Generate x values for the normal distribution curve based on the histogram edges
    x = np.linspace(edges[0], edges[-1], 300)

    # Calculates the probability density function (PDF) for the normal distribution based 
    # on the mean and standard deviation of the rebound heights
    pdf = (1 / (stddev * np.sqrt(2 * np.pi))) * np.exp(
    -0.5 * ((x - mean) / stddev) ** 2
    )

    # Scales the PDF by the number of data points(len(h3)) and the bin width to match the histogram
    bin_width = edges[1] - edges[0]
    plt.plot(x, pdf * len(h3) * bin_width, "g-", label="Normal model")

    # Add labels and title
    plt.xlabel('Rebound Height (cm)')
    plt.ylabel('Frequency')
    plt.title('Rebound Height Frequency')

    # Display the plot
    plt.show()

    # Plot histogram for coefficient of restitution
    plt.hist(e, bins=30, edgecolor='black', color='skyblue')
    
    # Add labels and title
    plt.xlabel('Coefficient of Restitution')
    plt.ylabel('Frequency')
    plt.title('Coefficient of Restitution Frequency')

    # Display the plot
    plt.show()

    # Q5 for 95% confidence interval
    z = 1.96  # z-value for 95% confidence interval
    rebound_height_ci = mean - z*stddev, mean + z*stddev
    print("95% Confidence Interval for Rebound Height:", rebound_height_ci)

    # Q5 for 95% confidence interval for coefficient of restitution
    e_ci = coeff_of_restitution - z*estddev, coeff_of_restitution + z*estddev
    print("95% Confidence Interval for Coefficient of Restitution:", e_ci)

main()