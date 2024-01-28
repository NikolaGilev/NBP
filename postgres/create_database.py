from sqlalchemy import create_engine
import psycopg2
import io


def main():
    engine = create_engine("postgresql+psycopg2://username:password@host:port/database")

    # Drop old table and create new empty table
    df.head(0).to_sql("table_name", engine, if_exists="replace", index=False)

    conn = engine.raw_connection()
    cur = conn.cursor()
    output = io.StringIO()
    df.to_csv(output, sep="\t", header=False, index=False)
    output.seek(0)
    contents = output.getvalue()
    cur.copy_from(output, "table_name", null="")  # null values become ''
    conn.commit()
    cur.close()
    conn.close()


def create_database():
    pass


if __name__ == "__main__":
    main()
