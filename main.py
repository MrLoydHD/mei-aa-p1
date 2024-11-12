import pickle
import time
import os
import csv
import pandas as pd
from algorithms.backtrackingSearch import BacktrackingSearch
from algorithms.exhaustiveSearch import ExhaustiveSearch
from algorithms.greedySearch import GreedySearch
from graph.generateGraph import generate_graph
from graph.saveGraphExample import save_graph_example
from utils.plots import plot_vertices_vs_search_time_greedy, plot_edge_prob_vs_search_time, plot_vertices_vs_tested_solutions, plot_vertices_vs_operations_count_greedy, plot_edge_prob_vs_max_clique_weight, plot_vertices_vs_max_clique_weight, plot_vertices_vs_search_time_exhaustive, plot_vertices_vs_operations_count_exhaustive, plot_vertices_vs_operations_count_075, plot_vertices_vs_search_time_075
from utils.utils import compare_greedy_backtracking_accuracy


def main(output_mode=False):
    
    #ask user for the algorithm to be used
    algorithm_name = input("Enter the algorithm number to be used: \n1. Exhaustive\n2. Greedy\n3. Backtracking\n")
    while algorithm_name not in ["1", "2", "3"]:
        algorithm_name = input("Invalid input. Please enter a valid algorithm number: \n1. Exhaustive\n2. Greedy\n3. Backtracking\n")
    if algorithm_name == "1":
        algorithm_name = "Exhaustive"
    elif algorithm_name == "2":
        algorithm_name = "Greedy"
    elif algorithm_name == "3":
        algorithm_name = "Backtracking"

    graphs = generate_all_graphs(501)
    run_simulation(graphs, output_mode, algorithm_name)
    
    # Load the CSV data for plotting
    csv_filename = f"results/{algorithm_name}_results.csv"
    data = pd.read_csv(csv_filename)
    
    # Generate and save plots
    plot_output_dir = f"results/plots/{algorithm_name}"
    os.makedirs(plot_output_dir, exist_ok=True)

    if algorithm_name == "Greedy":
        plot_vertices_vs_search_time_greedy(data, plot_output_dir)
        plot_vertices_vs_operations_count_greedy(data, plot_output_dir)
    elif algorithm_name == "Exhaustive":
        plot_vertices_vs_search_time_exhaustive(data, plot_output_dir)
        plot_vertices_vs_operations_count_exhaustive(data, plot_output_dir)
        plot_vertices_vs_operations_count_075(data, plot_output_dir)
        plot_vertices_vs_search_time_075(data, plot_output_dir)
        
    # Call the plotting functions
    plot_edge_prob_vs_search_time(data, plot_output_dir)
    plot_vertices_vs_tested_solutions(data, plot_output_dir)
    plot_edge_prob_vs_max_clique_weight(data, plot_output_dir)
    plot_vertices_vs_max_clique_weight(data, plot_output_dir)
    compare_greedy_backtracking_accuracy("results/Greedy_results.csv", "results/Backtracking_results.csv", "results/comparison")

def generate_all_graphs(max_vertices):
    if os.path.exists("graph/data/generated_graphs.pkl"):
        with open('graph/data/generated_graphs.pkl', 'rb') as f:
            return pickle.load(f)
    else:
        graphs = []
        print("Generating Graphs...")
        start = time.time()
        for vertices_count in range(5, max_vertices):
            for edges_probability in [0.125, 0.25, 0.5, 0.75]:
                G = generate_graph(vertices_count, edges_probability)
                graphs.append((G, edges_probability))  # Assegurar que cada elemento é (grafo, probabilidade)
                progress = vertices_count * 100 / max_vertices
                print(f"Progress (%): {round(progress, 2)}", end='\r')

                if vertices_count <= 10:  # Ajuste este limite conforme necessário
                    filename = f"graph_{vertices_count}_prob_{int(edges_probability*100)}.png"
                    save_graph_example(G, folder="results/graphExamples", filename=filename)
        end = time.time()
        print(f"Generated {len(graphs)} graphs in {end - start} seconds")
        
        # Salvar gráficos
        with open('graph/data/generated_graphs.pkl', 'wb') as f:
            pickle.dump(graphs, f)
        return graphs


def run_simulation(graphs, output_mode, algorithm_name):
    print(f"Max Weight Clique - {algorithm_name} Algorithm")
    print()

    # Configurar arquivos de saída
    txt_filename = f"results/{algorithm_name}_results.txt"
    csv_filename = f"results/{algorithm_name}_results.csv"

    # Limpar o arquivo TXT antes de começar a escrever, se estiver no modo de saída
    if output_mode:
        open(txt_filename, "w").close()

    # Abrir arquivo TXT para adicionar dados
    output_file = open(txt_filename, "a")

    # Criar diretório para CSV, se necessário
    os.makedirs(os.path.dirname(csv_filename), exist_ok=True)

    # Abrir o arquivo CSV e escrever cabeçalhos
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        headers = ["Vertices", "Edges_Prob", "Max_Weight", "Ops_Count", "Tested_Solutions", "Search_Time"]
        csv_writer.writerow(headers)

        # Escrever cabeçalhos no TXT
        if not output_mode:
            print("Vertices\tEdges_Prob.\tMax_Weight\tOps._Count\tTested_Solutions\tSearch_Time".expandtabs(30))
        else:
            output_file.write("Vertices\tEdges_Prob.\tMax_Weight\tOps._Count\tTested_Solutions\tSearch_Time\n".expandtabs(30))

        for graph_count, (graph, edges_prob) in enumerate(graphs, 1):
            vertices_count = graph.number_of_nodes()

            # Escolher algoritmo
            if algorithm_name == "Exhaustive":
                algorithm = ExhaustiveSearch(graph)
            elif algorithm_name == "Greedy":
                algorithm = GreedySearch(graph)
            elif algorithm_name == "Backtracking":
                algorithm = BacktrackingSearch(graph)
            else:
                raise NotImplemented()

            start_time_search = time.time()
            max_clique, operations_count, tested_solutions = algorithm.perform_search()
            end_time_search = time.time()

            search_delta_time = end_time_search - start_time_search

            # Criar resultado como lista de dados para CSV
            result = [
                vertices_count,
                edges_prob,
                max_clique.weight if max_clique else 0,
                operations_count,
                tested_solutions,
                search_delta_time
            ]

            # Escrever resultado no arquivo CSV
            csv_writer.writerow(result)

            # Formatar resultado para o TXT
            result_str = f"{vertices_count}\t{edges_prob}\t{result[2]}\t{operations_count}\t{tested_solutions}\t{search_delta_time}".expandtabs(30)

            # Escrever resultado no arquivo TXT e na tela, se não estiver no modo de saída
            if not output_mode:
                print(result_str)
            else:
                output_file.write(result_str + "\n")
                print(f"Progress (%): {round(graph_count * 100 / len(graphs), 2)}", end='\r')

            # Parar se o tempo de busca exceder 120 segundos
            if search_delta_time > 120:
                print("Stopped due to timeout...")
                break

    output_file.close()

if __name__ == "__main__":
    main(output_mode=True)