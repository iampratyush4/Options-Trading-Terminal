from py5paisa import FivePaisaClient
import pratyush
client = FivePaisaClient(cred=cred)
print(client.holdings())
