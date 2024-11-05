import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Define plotting functions and save them in the specified folder
def plot_vertices_vs_search_time(data, output_dir):
    plt.figure(figsize=(10, 6))
    for prob in data['Edges_Prob'].unique():
        subset = data[data['Edges_Prob'] == prob]
        mean_values = subset.groupby('Vertices')['Search_Time'].mean()
        std_dev = subset.groupby('Vertices')['Search_Time'].std()
        
        # Scatter plot for actual points with reduced opacity
        plt.scatter(mean_values.index, mean_values, alpha=0.3, label=f'Edges Prob = {prob}')
        
        # Quadratic fit with more prominent line
        z = np.polyfit(mean_values.index, mean_values, 2)
        p = np.poly1d(z)
        x_fit = np.linspace(mean_values.index.min(), mean_values.index.max(), 100)
        plt.plot(x_fit, p(x_fit), linewidth=2)  # Thicker, solid line
        
        # Fill standard deviation
        plt.fill_between(mean_values.index, mean_values - std_dev, mean_values + std_dev, alpha=0.2)

    plt.xlabel("Number of Vertices")
    plt.ylabel("Search Time (s)")
    plt.title("Number of Vertices vs. Search Time (with Quadratic Fit)")
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

def plot_vertices_vs_operations_count(data, output_dir):
    plt.figure(figsize=(10, 6))
    for prob in data['Edges_Prob'].unique():
        subset = data[data['Edges_Prob'] == prob]
        mean_values = subset.groupby('Vertices')['Ops_Count'].mean()
        
        # Scatter plot for actual points with reduced opacity
        plt.scatter(mean_values.index, mean_values, alpha=0.3, label=f'Edges Prob = {prob}')
        
        # Quadratic fit with more prominent line
        z = np.polyfit(mean_values.index, mean_values, 2)
        p = np.poly1d(z)
        x_fit = np.linspace(mean_values.index.min(), mean_values.index.max(), 100)
        plt.plot(x_fit, p(x_fit), linewidth=2)  # Thicker, solid line

    plt.xlabel("Number of Vertices")
    plt.ylabel("Operations Count")
    plt.title("Number of Vertices vs. Operations Count (with Quadratic Fit)")
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, "vertices_vs_operations_count.png"))
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