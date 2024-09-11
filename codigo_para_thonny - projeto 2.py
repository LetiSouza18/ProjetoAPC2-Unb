texto_port = """
|01 NOSSO POVO
|02 Aqui começa a história do tempo dos antigos 
|03 O início da história 
|04 Antes do mundo existir, Ngutapa já existia.
|05 se criou junto com ele.
|06 Baia era parente de Ngutapa.
|07 E no igarapé Tonetü.
|08 Naquele tempo, a terra ainda estava se formando. O mato era baixinho e o rio ainda tinha pouca água. Lá eles viviam.
|09 Passaram-se muitos anos.
|10 amarrou Mapana num pau, de braços e pernas abertos.
|11 Quando o mato já estava crescido
|12 Ngutapa foi caçar com Mapana
|14 Vieram as cabas e as formigas e morderam a sua periquita.
|16 Vovó, pode me desamarrar?
|17 Vovó, venha me desamarrar.
|18 Aquele desgraçado me prendeu aqui para me matar
|20 O cancã se transformou em gente,
|19 chegando mais perto, perguntou: O que lhe aconteceu, minha neta?
|21 Se você quiser se vingar
|22 está aqui a caba.
|23 Ela pegou a caba e guardou.
|24 Depois disso, o cancã se transformou em pássaro e foi embora.
|25 Vinha tocando flauta e pulava numa perna e noutra, cantando:
|26 Mapana estava esperando
|27 escondida num tronco de árvore,
|28 Desde que as cabas ferraram, seus joelhos começaram a inchar.
""" 

texto_ticuna = """
|01 TORÜ DUǕ'ǕGÜ
|02 Nori arü ügü ga ore ga nucüma'ǖ ga torü ga na nhunhaacü yi'i'ǖ.
|03 Norü ügü tchiga 
|04 Nüma ga Ngutapa ga naãne nama'ã ya ĩĩtchicü,
|06 Erü nüma ga Baia rü Ngutapa tanü'ǖ ni'ĩ
|05 rü wü'iva na yae.
|07 natü i Tonetü.
|08 Erü yeguma ãrü naãenecü rü wü'i i ngewaca i ya eaneǖrǖ'ǖ ni'ĩ yerü natauma ga nhãtü rü yema nawa nayemagüǖ ricatama ni'ĩ.
|09 marü nhurema ya taunecǖ na yemagü
|10 rü tauguma naãcü
|10/13 rü mu'utchicüma ya tauenecü na ngeacü.
|12 Rü yeguma fenewa tümamãã na u'ǖ ga namá ga Ngutapa,
|11 yerü yeguma rü marü nayaanegü ga naĩnecü
|14 rü maẽ rü tü'ǖ nawi rü ẽne rü tü'ü na ngo ga tümaãrü ngaǖwa.
|16 Pa noẽ, pa coou tautchiname'ǖ ega tchoǖ icuwẽgǖgu
|17 Pa noẽ tauchina meǖ ega tchoǖ icuiwẽgügu
|18 rü tchoǖ ni'ĩ ma i ucaǖǖtchi i Ngutapa nhãtagürü:
|20 Rü yeguma ga noẽ ga Co, co, co, cou rü ĩrü duǖ!
|21 Rü ngeguma cuütanütchaǖgu
|22 daani'ĩ ya maẽ nhanagürü
|23 yeguma rü inayau ga maẽ
|19 Rü yeguma ga noẽ i coou ta ngica itarü ĩ, rü ngiǖ ta ngaǖ rü cu tücü, pa tchauta'ã nhãtagürü:
|24 Rü marü yemawena ga coou rü tüna i ĩgü rü weriǖ ti'igüãrü.
|26 ngima ga Mapana rü marü iya nguẽẽ
|27 ga namacüwawa ga naĩpünewa
|25 rü nüma ga Ngutapa rü ni'ĩ woweruetchigü rü ni'ĩ wü'i paratchigü, rü ni'ĩ fenagütchigü,
|28 Rü yeguma ga nüma rü marü taguma i natchi rü nüma ga naãpüǖ rü marü manarütchaapüǖ,
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
# Seja bem-vindo e aproveite a leitura!                                        #
################################################################################
"""

print(texto_apresentacao)
lista = list()
dicionario = {}

for i in range(len(texto_port)):
    #Encontrar o número no texto em português
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
        
        #Armazenar em um dicionário o id, port, tic
        dicionario['port'] = frase_port
        dicionario['ticuna'] = frase_ticuna
        dicionario['id'] = i
        lista.append(dicionario)
        dicionario = {}
        
print(lista)




    
