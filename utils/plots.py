import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.metrics import r2_score

# GreedySearch
def plot_vertices_vs_operations_count_greedy(data, output_dir):
    plt.figure(figsize=(10, 6))
    for prob in data['Edges_Prob'].unique():
        subset = data[data['Edges_Prob'] == prob]
        mean_values = subset.groupby('Vertices')['Ops_Count'].mean()
        
        # Scatter plot for actual points with reduced opacity
        plt.scatter(mean_values.index, mean_values, alpha=0.3, label=f'Edges Prob = {prob}')
        
        # Quadratic fit
        x = mean_values.index
        y = mean_values.values
        z = np.polyfit(x, y, 2)  # Quadratic fit
        p = np.poly1d(z)
        y_fit = p(x)
        r_squared = r2_score(y, y_fit)  # Calculate R^2

        # Plot the quadratic fit
        x_fit = np.linspace(x.min(), x.max(), 100)
        plt.plot(x_fit, p(x_fit), linewidth=2, label=f'Quad Fit (Edges Prob = {prob}): $f(x) = {z[0]:.2e}x^2 + {z[1]:.2e}x + {z[2]:.2e}$, $R^2$ = {r_squared:.2f}')

    plt.xlabel("Number of Vertices")
    plt.ylabel("Operations Count")
    plt.title("Number of Vertices vs. Operations Count (Quadratic Fit)")
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, "vertices_vs_operations_count.png"))
    plt.close()

def plot_vertices_vs_search_time_greedy(data, output_dir):
    plt.figure(figsize=(10, 6))
    for prob in data['Edges_Prob'].unique():
        subset = data[data['Edges_Prob'] == prob]
        mean_values = subset.groupby('Vertices')['Search_Time'].mean()
        
        # Scatter plot for actual points with reduced opacity
        plt.scatter(mean_values.index, mean_values, alpha=0.3, label=f'Edges Prob = {prob}')
        
        # Quadratic fit
        x = mean_values.index
        y = mean_values.values
        z = np.polyfit(x, y, 2)  # Quadratic fit
        p = np.poly1d(z)
        y_fit = p(x)
        r_squared = r2_score(y, y_fit)  # Calculate R^2

        # Plot the quadratic fit
        x_fit = np.linspace(x.min(), x.max(), 100)
        plt.plot(x_fit, p(x_fit), linewidth=2, label=f'Quad Fit (Edges Prob = {prob}): $f(x) = {z[0]:.2e}x^2 + {z[1]:.2e}x + {z[2]:.2e}$, $R^2$ = {r_squared:.2f}')

    plt.xlabel("Number of Vertices")
    plt.ylabel("Search Time (s)")
    plt.title("Number of Vertices vs. Search Time (Quadratic Fit)")
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, "vertices_vs_search_time.png"))
    plt.close()


# ExhautiveSearch

# Function to plot Number of Vertices vs Operations Count with logarithmic scale for Exhaustive Search (Edges Prob = 0.75 only)
def plot_vertices_vs_operations_count_075(data, output_dir):
    plt.figure(figsize=(10, 6))

    # Filter data to only include edge probability 0.75
    subset = data[data['Edges_Prob'] == 0.75]
    mean_values = subset.groupby('Vertices')['Ops_Count'].mean()
    
    # Scatter plot for actual points
    plt.scatter(mean_values.index, mean_values, alpha=0.7, label='Edges Prob = 0.75', color='blue')
    
    # Exponential fit
    x = mean_values.index
    y = mean_values.values
    z = np.polyfit(x, np.log(y), 1)  # Linear fit on log of y for exponential fitting
    a = np.exp(z[1])  # Coefficient for the exponential base
    b = z[0]  # Exponent coefficient
    p = lambda x: a * np.exp(b * x)
    y_fit = p(x)
    r_squared = r2_score(y, y_fit)  # Calculate R^2

    # Plot the exponential fit
    x_fit = np.linspace(x.min(), x.max(), 100)
    plt.plot(x_fit, p(x_fit), linewidth=2, label=f'Exp Fit: $f(x) = {a:.2e} \cdot e^{{{b:.2e} \cdot x}}$, $R^2$ = {r_squared:.2f}', color='orange')

    plt.yscale('log')  # Apply logarithmic scale on y-axis
    plt.xlabel("Number of Vertices")
    plt.ylabel("Operations Count (log scale)")
    plt.title("Number of Vertices vs. Operations Count (Edges Prob = 0.75, Logarithmic Scale)")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)  # Apply grid to both major and minor ticks
    plt.savefig(os.path.join(output_dir, "vertices_vs_operations_count_075_log.png"))
    plt.close()

# Function to plot Number of Vertices vs Search Time with logarithmic scale for Exhaustive Search (Edges Prob = 0.75 only)
def plot_vertices_vs_search_time_075(data, output_dir):
    plt.figure(figsize=(10, 6))

    # Filter data to only include edge probability 0.75
    subset = data[data['Edges_Prob'] == 0.75]
    mean_values = subset.groupby('Vertices')['Search_Time'].mean()
    
    # Scatter plot for actual points
    plt.scatter(mean_values.index, mean_values, alpha=0.7, label='Edges Prob = 0.75', color='blue')
    
    # Exponential fit
    x = mean_values.index
    y = mean_values.values
    z = np.polyfit(x, np.log(y), 1)  # Linear fit on log of y for exponential fitting
    a = np.exp(z[1])  # Coefficient for the exponential base
    b = z[0]  # Exponent coefficient
    p = lambda x: a * np.exp(b * x)
    y_fit = p(x)
    r_squared = r2_score(y, y_fit)  # Calculate R^2

    # Plot the exponential fit
    x_fit = np.linspace(x.min(), x.max(), 100)
    plt.plot(x_fit, p(x_fit), linewidth=2, label=f'Exp Fit: $f(x) = {a:.2e} \cdot e^{{{b:.2e} \cdot x}}$, $R^2$ = {r_squared:.2f}', color='orange')

    plt.yscale('log')  # Apply logarithmic scale on y-axis
    plt.xlabel("Number of Vertices")
    plt.ylabel("Search Time (s) (log scale)")
    plt.title("Number of Vertices vs. Search Time (Edges Prob = 0.75, Logarithmic Scale)")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)  # Apply grid to both major and minor ticks
    plt.savefig(os.path.join(output_dir, "vertices_vs_search_time_075_log.png"))
    plt.close()



def plot_vertices_vs_operations_count_exhaustive(data, output_dir):
    plt.figure(figsize=(10, 6))
    for prob in data['Edges_Prob'].unique():
        subset = data[data['Edges_Prob'] == prob]
        mean_values = subset.groupby('Vertices')['Ops_Count'].mean()
        
        # Scatter plot for actual points with reduced opacity
        plt.scatter(mean_values.index, mean_values, alpha=0.3, label=f'Edges Prob = {prob}')
        
        # Exponential fit
        x = mean_values.index
        y = mean_values.values
        z = np.polyfit(x, np.log(y), 1)  # Linear fit on log of y for exponential fitting
        a = np.exp(z[1])  # Coefficient for the exponential base
        b = z[0]  # Exponent coefficient
        p = lambda x: a * np.exp(b * x)
        y_fit = p(x)
        r_squared = r2_score(y, y_fit)  # Calculate R^2

        # Plot the exponential fit
        x_fit = np.linspace(x.min(), x.max(), 100)
        plt.plot(x_fit, p(x_fit), linewidth=2, label=f'Exp Fit (Edges Prob = {prob}): $f(x) = {a:.2e} \cdot e^{{{b:.2e} \cdot x}}$, $R^2$ = {r_squared:.2f}')

    plt.xlabel("Number of Vertices")
    plt.ylabel("Operations Count")
    plt.title("Number of Vertices vs. Operations Count (Exponential Fit)")
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, "vertices_vs_operations_count.png"))
    plt.close()

def plot_vertices_vs_search_time_exhaustive(data, output_dir):
    plt.figure(figsize=(10, 6))
    for prob in data['Edges_Prob'].unique():
        subset = data[data['Edges_Prob'] == prob]
        mean_values = subset.groupby('Vertices')['Search_Time'].mean()
        
        # Scatter plot for actual points with reduced opacity
        plt.scatter(mean_values.index, mean_values, alpha=0.3, label=f'Edges Prob = {prob}')
        
        # Exponential fit
        x = mean_values.index
        y = mean_values.values
        z = np.polyfit(x, np.log(y), 1)  # Linear fit on log of y for exponential fitting
        a = np.exp(z[1])  # Coefficient for the exponential base
        b = z[0]  # Exponent coefficient
        p = lambda x: a * np.exp(b * x)
        y_fit = p(x)
        r_squared = r2_score(y, y_fit)  # Calculate R^2

        # Plot the exponential fit
        x_fit = np.linspace(x.min(), x.max(), 100)
        plt.plot(x_fit, p(x_fit), linewidth=2, label=f'Exp Fit (Edges Prob = {prob}): $f(x) = {a:.2e} \cdot e^{{{b:.2e} \cdot x}}$, $R^2$ = {r_squared:.2f}')

    plt.xlabel("Number of Vertices")
    plt.ylabel("Search Time (s)")
    plt.title("Number of Vertices vs. Search Time (Exponential Fit)")
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, "vertices_vs_search_time.png"))
    plt.close()


def plot_vertices_vs_tested_solutions(data, output_dir):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Vertices', y='Tested_Solutions', hue='Edges_Prob', data=data)
    plt.xlabel("Number of Vertices")
    plt.ylabel("Number of Tested Solutions")
    plt.title("Number of Vertices vs. Tested Solutions")
    plt.legend(title='Edges Prob', loc='upper left')
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, "vertices_vs_tested_solutions.png"))
    plt.close()

def plot_edge_prob_vs_search_time(data, output_dir):
    plt.figure(figsize=(10, 6))
    
    # Agrupar os vértices em intervalos para reduzir a quantidade de itens na legenda
    intervals = [(5, 10), (11, 15), (16, 20), (21, 25), (26, 28)]
    colors = ['blue', 'orange', 'green', 'red', 'purple']
    
    for i, (start, end) in enumerate(intervals):
        subset = data[(data['Vertices'] >= start) & (data['Vertices'] <= end)]
        plt.scatter(subset['Edges_Prob'], subset['Search_Time'], label=f'Vertices {start}-{end}', color=colors[i])
    
    plt.xlabel("Edge Probability")
    plt.ylabel("Search Time (s)")
    plt.title("Edge Probability vs. Search Time")
    
    # Ajuste da posição da legenda para deixá-la mais próxima do gráfico
    plt.legend(title="Vertex Range", loc='upper left', bbox_to_anchor=(1, 1), borderaxespad=0.5)
    
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, "edge_prob_vs_search_time_adjusted.png"), bbox_inches="tight")
    plt.close()

def plot_edge_prob_vs_max_clique_weight(data, output_dir):
    plt.figure(figsize=(10, 6))
    
    # Gráfico de barras agrupado por probabilidade de aresta e número de vértices
    sns.barplot(x="Edges_Prob", y="Max_Weight", hue="Vertices", data=data, palette="tab20")
    
    plt.xlabel("Edge Probability")
    plt.ylabel("Max Clique Weight")
    plt.title("Edge Probability vs. Max Clique Weight")
    
    # Ajuste da legenda para deixá-la mais compacta e ao lado do gráfico
    plt.legend(title="Vertices", loc='upper left', bbox_to_anchor=(1.05, 1), borderaxespad=0.5, ncol=2)
    
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, "edge_prob_vs_max_clique_weight_adjusted.png"), bbox_inches="tight")
    plt.close()

def plot_vertices_vs_max_clique_weight(data, output_dir):
    plt.figure(figsize=(10, 6))
    for prob in data['Edges_Prob'].unique():
        subset = data[data['Edges_Prob'] == prob]
        mean_values = subset.groupby('Vertices')['Max_Weight'].mean()
        
        # Scatter plot for actual points with reduced opacity
        plt.scatter(mean_values.index, mean_values, alpha=0.3, label=f'Edges Prob = {prob}')
        
        # Quadratic fit with more prominent line
        z = np.polyfit(mean_values.index, mean_values, 2)
        p = np.poly1d(z)
        x_fit = np.linspace(mean_values.index.min(), mean_values.index.max(), 100)
        plt.plot(x_fit, p(x_fit), linewidth=2)  # Thicker, solid line

    plt.xlabel("Number of Vertices")
    plt.ylabel("Max Clique Weight")
    plt.title("Number of Vertices vs. Max Clique Weight (with Quadratic Fit)")
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, "vertices_vs_max_clique_weight.png"))
    plt.close()