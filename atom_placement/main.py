"""
NAMES OF THE AUTHOR(S): Alice Burlats <alice.burlats@uclouvain.be>
Description: Benchmarking search strategies on vertex cover instances i01-i10.
"""

from search import *
import time

def run_benchmark(strategy_func, problem, step_limit, runs=10):
    """
    Exécute une stratégie sur un problème donné.
    Retourne la moyenne de la valeur, des étapes et du temps.
    """
    total_value = 0
    total_steps = 0
    total_time = 0

    for _ in range(runs):
        start_time = time.perf_counter()
        # On suppose que strategy_func retourne un objet avec .value() et .step
        node = strategy_func(problem, step_limit)
        elapsed = time.perf_counter() - start_time

        total_value += node.value()
        total_steps += node.step
        total_time += elapsed

    return (total_value / runs, total_steps / runs, total_time / runs)

if __name__ == '__main__':
    # Paramètres de l'expérience
    step_limit = 100
    nb_runs_random = 10
    output_filename = "results_benchmark.txt"
    
    # Génération de la liste des instances de i01 à i10
    instances = [f"instances/i{i:02d}.txt" for i in range(1, 11)]

    with open(output_filename, "w", encoding="utf-8") as log_file:
        # Création de l'en-tête du tableau
        header = f"{'Instance':<15} | {'Strategy':<22} | {'Avg Value':<10} | {'Avg Steps':<10} | {'Time (s)':<10}"
        separator = "-" * len(header)
        
        print(header)
        print(separator)
        log_file.write(header + "\n")
        log_file.write(separator + "\n")

        for inst_path in instances:
            try:
                # Initialisation du problème
                problem = AtomPlacement(inst_path)
                
                # Définition des stratégies à tester
                # Format: (fonction, est_aleatoire)
                strategies = [
                    (random_walk, True),
                    (max_value, False),
                    (randomized_max_value, True)
                ]

                for func, is_random in strategies:
                    # On ne lance 10 fois que si c'est aléatoire
                    runs = nb_runs_random if is_random else 1
                    
                    avg_val, avg_step, avg_time = run_benchmark(func, problem, step_limit, runs)
                    
                    # Formatage de la ligne de résultat
                    line = (f"{inst_path:<15} | {func.__name__:<22} | "
                            f"{avg_val:<10.2f} | {avg_step:<10.1f} | {avg_time:<10.5f}")
                    
                    print(line)
                    log_file.write(line + "\n")
                
                # Ligne de séparation pour la lisibilité entre les instances
                print(separator)
                log_file.write(separator + "\n")

            except FileNotFoundError:
                err = f"Fichier non trouvé : {inst_path}"
                print(err)
                log_file.write(err + "\n")
            except Exception as e:
                err = f"Erreur sur {inst_path} : {str(e)}"
                print(err)
                log_file.write(err + "\n")

    print(f"\nLe benchmark est terminé. Les résultats sont enregistrés dans : {output_filename}")