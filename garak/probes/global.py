# from garak.probes.vault.encoding2 import Codificacion                       # >100
# from garak.probes.vault.dan import Jailbreak                                # >100
# from garak.probes.vault.promptinject2 import SecuestroObjetivo              # >100






# misinformation
from garak.probes.vault.misleading import FalseAssertion50 as AfirmacionesFalsas    # 50
from garak.probes.vault.snowball import AlucinacionesParte1                        # > 67
from garak.probes.vault.packagehallucination import Python as AlucinacionesCodigo  # > 100


# speech
from garak.probes.vault.lmrc import Bullying                                                # 20
from garak.probes.vault.continuation import ContinueSlursReclaimedSlurs50 as Insultos       # 80
from garak.probes.vault.lmrc import Deadnaming                                              # 9
from garak.probes.vault.exclusion import ExclusionGender as ExclusionGenero    
from garak.probes.vault.lmrc import ContenidoSexual                                         # 20


# malicious 
from garak.probes.vault.malwaregen import Malware       # >100
from garak.probes.vault.scams import Scams as Estafas   # >100
from garak.probes.vault.others import Others as Otros   # 50