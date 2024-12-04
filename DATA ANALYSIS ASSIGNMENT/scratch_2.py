import matplotlib.pyplot as plt
import pandas as pd

# sampl data
data = {
    'sex': ['Male', 'Male', 'Male', 'Female', 'Female', 'Female', 'Male',
            'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female',
            'Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Breath Holding Time': [60.75, 67.41, 42.19, 59.74, 52.64, 43.37, 73.27,
                            59.09, 51.15, 58.32, 22.22, 30.57, 17.47, 22.39,
                            26.90, 36.85, 27.33, 29.55, 13.87, 34.66],
    'Height': [184, 182, 180, 191, 189, 181, 180, 170, 176, 185, 175, 158,
        166, 175, 160, 165, 166, 170, 170, 172],
    }
# Create a DataFrame
df = pd.DataFrame(data)

# set up the figure and axes
plt.figure(figsize=(14,6))

# Histogram of breath-holding times
plt.subplot(1, 2, 1)
plt.hist(df['Breath Holding Time'], bins=10, color='green', alpha=0.7, edgecolor='black')
plt.title('Histogram of Breath Holding Times')
plt.xlabel('Breath Holding Time')
plt.ylabel('Frequency')

#Side-by-side dot plot using scatter plot
plt.subplot(1,2,2)

#Plot for males
plt.scatter(df[df['sex']== 'Male']['Breath Holding Time'],
            [0] * sum(df['sex']== 'Male'),
            color='gold', label='Male', alpha=0.7)

#plot for females
plt.scatter(df[df['sex']== 'Female']['Breath Holding Time'],
            [1] * sum(df['sex']== 'Female'),
            color='blue', label='Female', alpha=0.7)

#customize the plot
plt.title('side-by-side Dot Plot of Breath Holding Times')
plt.yticks(ticks=[0,1], labels=['Male', 'Female'])
plt.xlabel('Breath Holding Time')
plt.legend()

#show the plots
plt.tight_layout()
plt.show()
