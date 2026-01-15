from diagrams import Cluster, Diagram
from diagrams.programming.language import Python

with Diagram(
        name="Mock Service Architecture",
        show=False,
        filename="mock",
        outformat="png",
        direction="TB"
):
    with Cluster("Mock"):
        mock_service = Python("mock-service")

    with Cluster("Users"):
        users_service = Python("users-service")

    with Cluster("Cards"):
        cards_service = Python("cards-service")

    with Cluster("Gateway"):
        gateway_service = Python("gateway-service")

    with Cluster("Accounts"):
        accounts_service = Python("accounts-service")

    gateway_service >> [users_service, cards_service, accounts_service]
    users_service >> [mock_service]
    cards_service >> [mock_service]
    accounts_service >> [mock_service]
