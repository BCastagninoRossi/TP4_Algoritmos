from graph import Graph
import csv
from itertools import combinations

MOVIE_TITLE_TYPE = "movie"
MOVIE_COLUMNS = ["tconst", "titleType", "primaryTitle"]
PRINCIPALS_COLUMNS = ["nconst", "category"]
MOVIES_DATA_PATH = "./datasets/title-basics-f.tsv"
ACTORS_DATA_PATH = "./datasets/title-principals-f.tsv"
ACTORS_NAMES_PATH = "./datasets/name-basics-f.tsv"


def read_data(movies_file, actors_file, actors_name_file):
    print("Reading data")
    movies_by_id = {}
    with open(movies_file, "r", newline="", encoding="utf-8") as file1:
        reader = csv.DictReader(file1, delimiter="\t")
        for row in reader:
            if row["titleType"] == MOVIE_TITLE_TYPE:
                movies_by_id[row['tconst']] = row

    actors_ids = set()
    actors_by_movie = {m: set() for m in movies_by_id.keys()}
    with open(actors_file, "r", newline="", encoding="utf-8") as file2:
        reader = csv.DictReader(file2, delimiter="\t")
        for row in reader:
            if row["tconst"] in actors_by_movie:
                actors_by_movie[row["tconst"]].update([row["nconst"]])
                actors_ids.update([row["nconst"]])

    actor_names_by_id = {}
    with open(actors_name_file, "r", newline="", encoding="utf-8") as file2:
        reader = csv.DictReader(file2, delimiter="\t")
        for row in reader:
            if row["nconst"] in actors_ids:
                actor_names_by_id[row["nconst"]] = row["primaryName"]

    return movies_by_id, actors_by_movie, actor_names_by_id


# ACTORS BY MOVIE ES UN DICCIONARIO CON KEYS STR CON EL MOVIE ID Y VALUE UNA LISTA CON LOS ACTORS ID QUE ACTUARON EN CADA UNA
# MOVIES BY ID ES UN DICCIONARIO CON KEYS SRT CON EL MOVIE ID Y VALUE UN DICT CON MIL PARÁMETROS DE CADA PELÍCULA, PERO NO CONTIENE A LOS ACTORES
#ACTOR NAMES BY ID ES UN DICCIONARIO con keys con el actor ID y value el string con el nombre de cada actor

def load_graph_b(movies_by_id, actors_by_movie, actor_names_by_id) -> Graph:
    graph = Graph()
    print("Loading graph B")

    count = 0

    # Add vertices to the graph
    for movie_id in movies_by_id.keys():
        movie_title = movies_by_id[movie_id]['primaryTitle']
        if not graph.vertex_exists(movie_id):
            graph.add_vertex(movie_id, movie_title)

    for actor_id in actor_names_by_id.keys():
        if not graph.vertex_exists(actor_id):
            graph.add_vertex(actor_id, actor_names_by_id.get(actor_id, "ERROR"))

    # Add edges to the graph
    for movie_id in actors_by_movie.keys():
        for actor_id in actors_by_movie[movie_id]:
            if not graph.edge_exists(actor_id, movie_id):
                if not graph.vertex_exists(actor_id):
                #Realizo este chequeo porque aparentemente en la base de title_principals hay películas relacionadas con id's de actores que no se encuentran presentes en la base de actores.
                    graph.add_vertex(actor_id, "NO DATA PROVIDED")
                graph.add_edge(actor_id, movie_id)

    return graph


movies_by_id, actors_by_movie, actor_names_by_id = read_data(MOVIES_DATA_PATH, ACTORS_DATA_PATH, ACTORS_NAMES_PATH)
graph = load_graph_b(movies_by_id, actors_by_movie, actor_names_by_id)
# graph.print_graph()
