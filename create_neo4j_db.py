from neo4j import GraphDatabase
import os

uri = "bolt://localhost:7687"
username = "neo4j"
password = "password"
query_folder = "./neo4j"
query_relations_folder = query_folder + "/relationships"


def run_query(tx, query):
    tx.run(query)


def execute_queries(session, query_files):
    with session.begin_transaction() as tx:
        for query_file in query_files:
            query_path = os.path.join(query_folder, query_file)
            with open(query_path, "r") as file:
                cypher_query = file.read()
                try:
                    tx.run(cypher_query)
                except Exception as e:
                    print(f"Error executing query in file {query_file}: {str(e)}")
                    tx.rollback()
                    break
        else:
            tx.commit()


with GraphDatabase.driver(uri, auth=(username, password)) as driver:
    with driver.session() as session:
        try:
            query_files = [
                file for file in os.listdir(query_folder) if file.endswith(".cql")
            ]
            query_relations_files = [
                file
                for file in os.listdir(query_relations_folder)
                if file.endswith(".cql")
            ]

            execute_queries(session, query_files)
            execute_queries(session, query_relations_files)
        except Exception as e:
            print(f"Error during execution: {str(e)}")
