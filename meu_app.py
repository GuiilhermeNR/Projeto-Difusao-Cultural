import streamlit as st
from PIL import Image

st.set_page_config(page_title='Projeto Ação Cultural')
st.subheader('Difusão Cultural')
(st.title('Oque é ?'))
st.write('É um processo, na dinâmica cultutral, \nem que os elementos ou complexos culturais se difundem de uma sociedade a outra A Difusão Cultural está centrada em ações de democratização do acesso aos bens culturais, formação de público e oferta de subsídios de estímulo ao conhecimento, reconhecimento e valorização dos bens, para instituições culturais e de ensino. A Educação Patrimonial tem sua metodologia pautada na construção do conhecimento a partir do estímulo à reflexão sobre a história, a memória, a identidade e os patrimônios locais.')
im = Image.open('thumbnail.png.jpg')
st.image(im)
with st.container():
      st.write('---')
      st.title('Importancia')
      st.write('A difusão cultural desempenha um papel crucial na construção de identidades culturais e no enriquecimento das sociedades. Ela permite que diferentes culturas se conectem, compartilhem conhecimentos e experiências, promovendo a diversidade e a compreensão mútua.\n Através da difusão cultural, as pessoas têm a oportunidade de conhecer e apreciar diferentes formas de arte, música, dança, culinária e outras expressões culturais. Isso contribui para a preservação e valorização das tradições e patrimônios culturais de cada comunidade.')
      im1 = Image.open('importancia.jpg')
      st.image(im1)
with st.container():
      st.write('---')
      st.title('Processos Difusão Cultural ')
      st.write('A difusão cultural pode ocorrer de várias maneiras, incluindo migração, comércio, turismo, meios de comunicação e tecnologia. A migração, por exemplo, é um dos principais impulsionadores da difusão cultural, pois as pessoas levam consigo suas tradições e práticas culturais ao se deslocarem para novos lugares. O comércio também desempenha um papel importante na difusão cultural, pois permite a troca de bens e ideias entre diferentes culturas. O turismo, por sua vez, possibilita que as pessoas experimentem e se envolvam com culturas diferentes da sua própria, promovendo a compreensão e o respeito mútuo.')
      im2 = Image.open('processos.jpg')
      st.image(im2)
with st.container():
      st.write('---')
      st.title('Impactos da Difusão Cultural')
      st.write('A difusão cultural pode ter impactos positivos e negativos nas sociedades. Por um lado, ela pode promover a diversidade cultural, o diálogo intercultural e a tolerância. Por outro lado, também pode levar à perda de identidade cultural e à homogeneização cultural. Em alguns casos, a difusão cultural pode levar à assimilação cultural, onde uma cultura dominante absorve e suprime as características de uma cultura minoritária. Isso pode resultar na perda de línguas, tradições e práticas culturais únicas.')
      im3 = Image.open('impactos.jpg')
      st.image(im3)
with st.container():
      st.write('---')
      st.title('Exemplos de Difusão Cultural')
      st.write('A história está repleta de exemplos de difusão cultural. Um exemplo clássico é a difusão da cultura grega durante o período helenístico, quando o Império Macedônico de Alexandre, o Grande, conquistou vastas áreas do mundo conhecido na época. A cultura grega, com sua filosofia, arte, arquitetura e língua, foi disseminada por todo o império, influenciando profundamente as culturas locais. Da mesma forma, a difusão cultural ocorreu durante o período de colonização europeia, quando as culturas europeias foram trazidas para as Américas, África e Ásia. Ou até mesmo bem mais próximo de nós como carnaval, festa junina, ou samba.')
      im4 = Image.open('samba.jpg')
      st.image(im4)
with st.container():
      st.write('---')
      st.subheader('Ficou com Alguma dúvida ?')
      st.write('O Chat pode ajudar você! [Falar com CHAT](https://chatgpt.com/?oai-dm=1)')