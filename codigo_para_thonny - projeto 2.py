import json

texto_port = """
|00 NOSSO POVO
|01 Aqui começa a história do tempo dos antigos 
|02 O início da história 
|03 Antes do mundo existir, Ngutapa já existia.
|04 se criou junto com ele.
|05 Baia era parente de Ngutapa.
|06 E no igarapé Tonetü.
|07 Naquele tempo, a terra ainda estava se formando. O mato era baixinho e o rio ainda tinha pouca água. Lá eles viviam.
|08 Passaram-se muitos anos.
|09 amarrou Mapana num pau, de braços e pernas abertos.
|10 Quando o mato já estava crescido
|11 Ngutapa foi caçar com Mapana
|12 Vieram as cabas e as formigas e morderam a sua periquita.
|13 Vovó, pode me desamarrar?
|14 Vovó, venha me desamarrar.
|15 Aquele desgraçado me prendeu aqui para me matar
|17 O cancã se transformou em gente,
|16 chegando mais perto, perguntou: O que lhe aconteceu, minha neta?
|18 Se você quiser se vingar
|19 está aqui a caba.
|20 Ela pegou a caba e guardou.
|21 Depois disso, o cancã se transformou em pássaro e foi embora.
|22 Vinha tocando flauta e pulava numa perna e noutra, cantando:
|23 Mapana estava esperando
|24 escondida num tronco de árvore,
|25 Desde que as cabas ferraram, seus joelhos começaram a inchar.
""" 

texto_ticuna = """
|00 TORÜ DUǕ'ǕGÜ
|01 Nori arü ügü ga ore ga nucüma'ǖ ga torü ga na nhunhaacü yi'i'ǖ.
|02 Norü ügü tchiga 
|03 Nüma ga Ngutapa ga naãne nama'ã ya ĩĩtchicü,
|05 Erü nüma ga Baia rü Ngutapa tanü'ǖ ni'ĩ
|04 rü wü'iva na yae.
|06 natü i Tonetü.
|07 Erü yeguma ãrü naãenecü rü wü'i i ngewaca i ya eaneǖrǖ'ǖ ni'ĩ yerü natauma ga nhãtü rü yema nawa nayemagüǖ ricatama ni'ĩ.
|08 marü nhurema ya taunecǖ na yemagü
|09 rü tauguma naãcü rü mu'utchicüma ya tauenecü na ngeacü.
|11 Rü yeguma fenewa tümamãã na u'ǖ ga namá ga Ngutapa,
|10 yerü yeguma rü marü nayaanegü ga naĩnecü
|12 rü maẽ rü tü'ǖ nawi rü ẽne rü tü'ü na ngo ga tümaãrü ngaǖwa.
|13 Pa noẽ, pa coou tautchiname'ǖ ega tchoǖ icuwẽgǖgu
|14 Pa noẽ tauchina meǖ ega tchoǖ icuiwẽgügu
|15 rü tchoǖ ni'ĩ ma i ucaǖǖtchi i Ngutapa nhãtagürü:
|17 Rü yeguma ga noẽ ga Co, co, co, cou rü ĩrü duǖ!
|18 Rü ngeguma cuütanütchaǖgu
|19 daani'ĩ ya maẽ nhanagürü
|20 yeguma rü inayau ga maẽ
|16 Rü yeguma ga noẽ i coou ta ngica itarü ĩ, rü ngiǖ ta ngaǖ rü cu tücü, pa tchauta'ã nhãtagürü:
|21 Rü marü yemawena ga coou rü tüna i ĩgü rü weriǖ ti'igüãrü.
|23 ngima ga Mapana rü marü iya nguẽẽ
|24 ga namacüwawa ga naĩpünewa
|22 rü nüma ga Ngutapa rü ni'ĩ woweruetchigü rü ni'ĩ wü'i paratchigü, rü ni'ĩ fenagütchigü,
|25 Rü yeguma ga nüma rü marü taguma i natchi rü nüma ga naãpüǖ rü marü manarütchaapüǖ,
"""


texto_apresentacao = """
################################################################################
# Disciplina: Algoritmos e programação de computadores                         # 
# Docentes: Edison Ishikawa e Maristela de Holanda                             #
# Discentes: André Guil, Gabriella Caetano e Letícia Souza                     #
#                                                                              #  
#-------------------------------Projeto 2--------------------------------------#
#                                                                              #
# ESTE PROGRAMA APRESENTA POR MEIO DE UM DICIONÁRIO FRASES EM PORTUGUÊS E      #
# FRASES NA LINGUAGEM TICUNA QUE POSSUEM O MESMO SENTIDO.                      #
#                                                                              #
################################################################################

Seja bem-vindo(a) e aproveite a leitura!
"""

print(texto_apresentacao)
lista = list()
dicionario = {}
translation = dict()

for i in range(len(texto_port)):
    #Encontrar o número no texto em português depois do caracter de marcação
    if texto_port[i] == '|':
        #Achar a frase em português correspondente a esse número:
        num = texto_port[i + 1] + texto_port[i + 2]
        pos_num_port = int(texto_port.find(num))
        pos_prox_num_port = int(texto_port.find(str(int(num) + 1)))
        tam_frase_port = pos_prox_num_port - pos_num_port
        frase_port =  texto_port[pos_num_port + 2 : pos_num_port + tam_frase_port - 3] 
        
        #Achar a frase em ticuna correpondente a esse número:
        pos_num_ticuna = int(texto_ticuna.find(num))
        pos_prox_num_ticuna = int(texto_ticuna.find(str(int(num) + 1)))
        tam_frase_ticuna = pos_prox_num_ticuna - pos_num_ticuna
        frase_ticuna =  texto_ticuna[pos_num_ticuna + 2 : pos_num_ticuna + tam_frase_ticuna - 3] 
        
        #Armazenar no dicionário o id e o translation (que é um dict com as chaves pt e tca)
        dicionario['id'] = int(num)
        translation['pt'] = frase_port
        translation['tca'] = frase_ticuna
        dicionario['translation'] = translation
        lista.append(dicionario)
        dicionario = {}

print(json.dumps(lista, indent=2, ensure_ascii=False))




    
