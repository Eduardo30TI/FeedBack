import streamlit as st
from streamlit_js_eval import streamlit_js_eval
import time
from Gmail import Mail


st.set_page_config(page_title='DeMarchi SP',page_icon='logo.png',layout='centered')

def main():

    placeholder=st.empty()

    temp_dict=dict()
    with placeholder.container():

        st.header('Sugestões ou Reclamações')
        st.markdown('----')
        
        temp_dict['assunto']=st.text_input('Assunto',placeholder='Informe o assunto para direcionarmos para o setor responsável')        
        temp_dict['mensagem']=st.text_area('Feedback',height=350)

        #files=st.file_uploader('Anexo')

        btn=st.button('Enviar',type='primary')
        
        pass


    if btn==True:

        resp=verificarCampo(temp_dict)

        if resp[0]!=None:

            mensagem=st.warning(resp[0])
            time.sleep(1)
            mensagem.empty()

            pass

        else:

            mail=Mail()

            send_dict={'To':['ti@demarchisaopaulo.com.br'],'CC':[''],'Anexo':[]}

            mensagem='\n'.join([f'<p>{m.strip()}</p>' for m in temp_dict['mensagem'].split('\n')])
            print(mensagem)      

            mail.Enviar(assunto=temp_dict['assunto'],mensagem=mensagem,info=send_dict)

            mensagem=st.success('E-mail enviado com sucesso')
            time.sleep(1)
            mensagem.empty()
            time.sleep(1)
            #streamlit_js_eval(js_expressions='parent.window.location.reload()')

            pass

        pass

    pass


def verificarCampo(campos:dict):

    temp_dict=dict()

    temp_dict[0]=None
    for k,v in campos.items():

        if v=='':

            temp_dict[0]=f'Informe {k}'

            break

        pass

    return temp_dict

    pass


if __name__=='__main__':

    main()

    pass