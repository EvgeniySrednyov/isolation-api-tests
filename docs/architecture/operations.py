from diagrams import Cluster, Diagram
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.queue import Kafka
from diagrams.programming.language import Python

with Diagram(
        name="Operations Service Architecture",
        show=False,
        filename="operations",
        outformat="png",
        direction="TB"
):
    kafka = Kafka("kafka")
    postgres = PostgreSQL("postgres")

    with Cluster("Operations"):
        operations_service = Python("operations-service")
        operations_processor = Python("operations-processor")

    operations_service >> [postgres]
    operations_processor >> [kafka, postgres]
