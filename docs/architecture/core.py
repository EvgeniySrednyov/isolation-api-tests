from diagrams import Cluster, Diagram
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.queue import Kafka
from diagrams.programming.language import Python

with Diagram(
        name="Service Architecture",
        show=False,
        filename="core",
        outformat="png",
        direction="TB"
):
    kafka = Kafka("kafka")
    postgres = PostgreSQL("postgres")

    with Cluster("Users"):
        users_service = Python("users-service")

    with Cluster("Cards"):
        cards_service = Python("cards-service")

    with Cluster("Gateway"):
        gateway_service = Python("gateway-service")

    with Cluster("Accounts"):
        accounts_service = Python("accounts-service")

    with Cluster("Operations"):
        operations_service = Python("operations-service")
        operations_processor = Python("operations-processor")

    gateway_service >> [users_service, cards_service, accounts_service]
    operations_service >> [postgres]
    operations_processor >> [kafka, postgres]
