import pandas as pd
import matplotlib.pyplot as plt
import os

def compare_greedy_backtracking_accuracy(greedy_csv_path, backtracking_csv_path, output_dir):
    # Load the CSV files
    greedy_df = pd.read_csv(greedy_csv_path)
    backtracking_df = pd.read_csv(backtracking_csv_path)

    # Merge the two dataframes on vertices and edges probability to align results
    comparison_df = pd.merge(greedy_df, backtracking_df, on=["Vertices", "Edges_Prob"], suffixes=('_greedy', '_backtracking'))

    # Calculate the difference (delta) and accuracy percentage for each entry
    comparison_df['Delta'] = comparison_df['Max_Weight_backtracking'] - comparison_df['Max_Weight_greedy']
    comparison_df['Accuracy (%)'] = (comparison_df['Max_Weight_greedy'] / comparison_df['Max_Weight_backtracking']) * 100

    # Rename and reorder columns as specified
    comparison_df = comparison_df.rename(columns={
        'Vertices': 'Graph',
        'Max_Weight_backtracking': 'Backtracking Weight',
        'Max_Weight_greedy': 'Greedy Weight'
    })
    comparison_df = comparison_df[['Graph', 'Edges_Prob', 'Backtracking Weight', 'Greedy Weight', 'Delta', 'Accuracy (%)']]

    # Calculate total accuracy (mean of the 'Accuracy (%)' column) and add as a final row
    total_accuracy = comparison_df['Accuracy (%)'].mean()
    total_row = pd.DataFrame([["Total", "", "", "", "", total_accuracy]], columns=comparison_df.columns)
    comparison_df = pd.concat([comparison_df, total_row], ignore_index=True)

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Save the comparison table as both CSV and TXT
    comparison_csv_path = os.path.join(output_dir, 'greedy_vs_backtracking_accuracy.csv')
    comparison_txt_path = os.path.join(output_dir, 'greedy_vs_backtracking_accuracy.txt')
    comparison_df.to_csv(comparison_csv_path, index=False)
    
    with open(comparison_txt_path, 'w') as f:
        f.write(comparison_df.to_string(index=False))

    # Filter data for plotting, focusing only on real data (not "Total" row)
    filtered_df = comparison_df[comparison_df['Graph'] != "Total"]

    # Plot: Separate plot for each edge probability, showing only mismatched values
    for prob in filtered_df['Edges_Prob'].unique():
        subset = filtered_df[(filtered_df['Edges_Prob'] == prob) & (filtered_df['Delta'] != 0)]

        # Create figure
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Plot only points with different Greedy and Backtracking weights
        for idx, row in subset.iterrows():
            backtracking_y = row['Backtracking Weight']
            greedy_y = row['Greedy Weight']
            graph_x = row['Graph']

            # Draw a faint line between Backtracking and Greedy points
            ax.plot([graph_x, graph_x], [backtracking_y, greedy_y], color='gray', linestyle='--', alpha=0.5)

            # Plot Backtracking and Greedy points
            ax.scatter(graph_x, backtracking_y, color='blue', label='Backtracking' if idx == 0 else "", alpha=0.7)
            ax.scatter(graph_x, greedy_y, color='orange', label='Greedy' if idx == 0 else "", alpha=0.7)

        ax.set_xlabel('Number of Vertices (Graph)')
        ax.set_ylabel('Clique Weight')
        ax.set_title(f'Comparison of Greedy vs. Backtracking Weights (Edges Prob = {prob})')
        
        # Add a legend
        ax.legend(loc='upper left', title='Legend', labels=['Difference Line', 'Greedy Weight', 'Backtracking Weight'])
        
        ax.grid(True)

        # Save the plot for each probability level
        plot_path = os.path.join(output_dir, f'greedy_vs_backtracking_weight_comparison_prob_{prob}.png')
        plt.savefig(plot_path)
        plt.close()

    print(f"Comparison files saved to: {comparison_csv_path}, {comparison_txt_path}, plots in {output_dir}")

# Example usage in main:
# compare_greedy_backtracking_accuracy('/path/to/Greedy_results.csv', '/path/to/Backtracking_results.csv', '/path/to/output_dir')
