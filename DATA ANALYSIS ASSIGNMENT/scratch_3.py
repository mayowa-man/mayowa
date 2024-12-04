import pandas as pd
import matplotlib.pyplot as plt

#sample data
data = {
    'Music': [304, 257, 174, 214,69,
              317, 387, 47, 157, 0,
              332, 308, 317, 286, 236,
              299, 206, 278, 188, 43,
              0, 0, 0, 0, 0],
    'No Music': [292, 270, 47, 288, 324,
                 292, 364, 316, 287, 75,
                 282, 149, 274, 319,213,
                 3, 324, 2, 128, 219,
                 94, 164, 0, 0, 0],
}

df = pd.DataFrame(data)

#step 1: create histogram
plt.figure(figsize=(12, 6))

# histogram for music
plt.subplot(1, 2, 1)
plt.hist(df['Music'], bins=10, color='green', alpha=0.7, edgecolor='black')
plt.title('Histogram of Plant Growth With Music')
plt.xlabel('Growth')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)


# histogram for no music
plt.subplot(1, 2, 2)
plt.hist(df['No Music'], bins=10, color='blue', alpha=0.7, edgecolor='black')
plt.title('Histogram of Plant Growth Without Music')
plt.xlabel('Growth')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)

plt.tight_layout()
plt.show()

# step 2: create dot plots
plt.figure(figsize=(10, 5))

# dot plot for music
plt.subplot(1, 2, 1)
plt.scatter(df['Music'], [0] * len(df['Music']), color='orange', alpha=0.7)
plt.title('Dot Plot of Plant Growth With Music')
plt.yticks([])
plt.xlabel('Growth')
plt.axhline(y=0,color='black', lw=0.5 )

# dot plot for no music
plt.subplot(1, 2, 2)
plt.scatter(df['No Music'], [0] * len(df['No Music']), color='blue', alpha=0.7)
plt.title('Dot Plot of Plant Growth Without Music')
plt.yticks([])
plt.xlabel('Growth')
plt.axhline(y=0,color='black', lw=0.5 )

plt.tight_layout()
plt.show()






















