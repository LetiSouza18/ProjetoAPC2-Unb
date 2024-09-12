import json

texto_port = "NOSSO POVO|Aqui começa a história do tempo dos antigos|O início da história|Antes do mundo existir, Ngutapa já existia.|se criou junto com ele.|Baia era parente de Ngutapa.|E no igarapé Tonetü.|Naquele tempo, a terra ainda estava se formando. O mato era baixinho e o rio ainda tinha pouca água. Lá eles viviam.|Passaram-se muitos anos.|amarrou Mapana num pau, de braços e pernas abertos.|Quando o mato já estava crescido|Ngutapa foi caçar com Mapana|Vieram as cabas e as formigas e morderam a sua periquita.|Vovó, pode me desamarrar?|Vovó, venha me desamarrar.|Aquele desgraçado me prendeu aqui para me matar|chegando mais perto, perguntou: O que lhe aconteceu, minha neta?|O cancã se transformou em gente,|Se você quiser se vingar|está aqui a caba.|Ela pegou a caba e guardou.|Depois disso, o cancã se transformou em pássaro e foi embora.|Vinha tocando flauta e pulava numa perna e noutra, cantando:|Mapana estava esperando|escondida num tronco de árvore,|Desde que as cabas ferraram, seus joelhos começaram a inchar."
texto_ticuna = "TORÜ DUǕ'ǕGÜ|Nori arü ügü ga ore ga nucüma'ǖ ga torü ga na nhunhaacü yi'i'ǖ.|Norü ügü tchiga|Nüma ga Ngutapa ga naãne nama'ã ya ĩĩtchicü,|rü wü'iva na yae.|Erü nüma ga Baia rü Ngutapa tanü'ǖ ni'ĩ|natü i Tonetü.|Erü yeguma ãrü naãenecü rü wü'i i ngewaca i ya eaneǖrǖ'ǖ ni'ĩ yerü natauma ga nhãtü rü yema nawa nayemagüǖ ricatama ni'ĩ.|marü nhurema ya taunecǖ na yemagü|rü tauguma naãcü rü mu'utchicüma ya tauenecü na ngeacü.|yerü yeguma rü marü nayaanegü ga naĩnecü|Rü yeguma fenewa tümamãã na u'ǖ ga namá ga Ngutapa,|rü maẽ rü tü'ǖ nawi rü ẽne rü tü'ü na ngo ga tümaãrü ngaǖwa.|Pa noẽ, pa coou tautchiname'ǖ ega tchoǖ icuwẽgǖgu|Pa noẽ tauchina meǖ ega tchoǖ icuiwẽgügu|rü tchoǖ ni'ĩ ma i ucaǖǖtchi i Ngutapa nhãtagürü:|Rü yeguma ga noẽ i coou ta ngica itarü ĩ, rü ngiǖ ta ngaǖ rü cu tücü, pa tchauta'ã nhãtagürü:|Rü yeguma ga noẽ ga Co, co, co, cou rü ĩrü duǖ!|Rü ngeguma cuütanütchaǖgu|daani'ĩ ya maẽ nhanagürü|yeguma rü inayau ga maẽ|Rü marü yemawena ga coou rü tüna i ĩgü rü weriǖ ti'igüãrü.|rü nüma ga Ngutapa rü ni'ĩ woweruetchigü rü ni'ĩ wü'i paratchigü, rü ni'ĩ fenagütchigü,|ngima ga Mapana rü marü iya nguẽẽ|ga namacüwawa ga naĩpünewa|Rü yeguma ga nüma rü marü taguma i natchi rü nüma ga naãpüǖ rü marü manarütchaapüǖ,"


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
dicionario = dict()
translation = dict()

listPt = texto_port.split('|')
listTca = texto_ticuna.split('|')

for i in range(len(listPt)):     
        #Armazenar no dicionário o id e o translation (que é um dict com as chaves pt e tca)
        dicionario['id'] = i
        translation['pt'] = listPt[i]
        translation['tca'] = listTca[i]
        dicionario['translation'] = translation
        lista.append(dicionario)
        translation = {}
        dicionario = {}

print(json.dumps(lista, indent=2, ensure_ascii=False))




    
