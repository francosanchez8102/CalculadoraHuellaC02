import streamlit as st
from constantes import FACTORES

lista_factores = FACTORES

def calcula_huella(*arguments):
    """
    Esta función calcula la huella de carbono
    Parameters
    ----------
    *arguments: int
    Lista con los consumos por categoría
    """
    totalSum = 0
    for (number, factor) in zip(arguments, lista_factores):
        totalSum += number * factor
    return totalSum

def obtener_impacto_arboles(huella):
    arboles_por_tonelada = 3.67 # Cantidad promedio de árboles necesarios para compensar una tonelada de emisiones de CO2
    arboles_necesarios = (huella / 1000) * arboles_por_tonelada # Convertir huella a toneladas
    print(huella)

    return arboles_necesarios

def obtener_impacto_ejemplos():
    impacto = {
        "Impacto en el cambio climático": "La huella de carbono generada contribuye al cambio climático, aumentando la temperatura promedio del planeta.",
        "Contaminación del aire": "Las emisiones de carbono también se asocian con la contaminación del aire y problemas de salud, como enfermedades respiratorias.",
        "Escasez de recursos naturales": "El aumento de las emisiones de carbono puede agotar los recursos naturales, como el agua y los combustibles fósiles.",
        "Degradación del ecosistema": "La emisión de carbono puede afectar negativamente a los ecosistemas, provocando la pérdida de biodiversidad y daños a los hábitats naturales."
    }
    return impacto



def obtener_compensacion_ejemplos():
    compensacion = ["Reducir el consumo de carne y productos lácteos.",
                    "Optar por fuentes de energía renovable.",
                    "Utilizar el transporte público, bicicleta o caminar en lugar de utilizar vehículos particulares.",
                    "Reducir el consumo de agua.",
                    "Reducir el consumo de electricidad optando por lámparas de bajo consumo o adquiriendo electrodomésticos de bajo consumo.",
                    "Reducir la cantidad de residuos generados, reutilizando envases y reciclando materiales como latas de aluminio, papel, cartón y vidrios."
    ]
    return compensacion

st.title("Calculadora Huella de Carbono :earth_americas:")

# Efecto de la huella de carbono en el medio ambiente
st.subheader("**:blue[¿Cómo afecta la Huella de Carbono al medio ambiente?]**")

for ejemplo, mensaje in obtener_impacto_ejemplos().items():
    st.write(f"- **{ejemplo}:** {mensaje}")

# Formulario
st.subheader("**:blue[Ingresa tus datos de consumo SEMANALES]**")
with st.form("my_form"):

    with st.expander("Medios de transporte"):
            # Elementos dentro del expander
            st.write("En promedio, cuantos km por semana recorres utilizando cada uno de estos medios de transporte?")
            km_auto = st.number_input("km en automóvil ", min_value=0, format="%.2f")
            km_moto = st.number_input("km en moto", min_value=0, format="%.2f")
            km_colect_die = st.number_input("km en colectivo", min_value=0, format="%.2f")
                    
    
    with st.expander("Electrodomesticos"):
            # Elementos dentro del expander
            st.write("En promedio, cuantas hs por día utilizas cada uno de estos electrodomésticos? ")
            hs_tele = st.number_input("Horas televisor", min_value=0, format="%.2f")
            hs_aire = st.number_input("Horas aire acondicionado", min_value=0, format="%.2f")
            hs_ventilador = st.number_input("Horas ventilador", min_value=0, format="%.2f")
            hs_heladera = 24
            hs_lavarropa = st.number_input("Horas lavarropa", min_value=0, format="%.2f")
            hs_plancha = st.number_input("Horas plancha", min_value=0, format="%.2f")
            hs_horno_elect = st.number_input("Horas horno electrico", min_value=0, format="%.2f")
            hs_microondas = st.number_input("Horas microondas", min_value=0, format="%.2f")

        
    with st.expander("Alimentos"):
            # Elementos dentro del expander
            st.write("En promedio, cuanta cantidad en gr/l comes de cada uno de estos alimentos por semana? ")
            kg_carne_vaca = st.number_input("Gramos de carne de vaca", min_value=0, format="%.2f")
            kg_carne_cerdo = st.number_input("Gramos de carne de cerdo", min_value=0,format="%.2f")
            kg_pollo = st.number_input("Gramos de pollo", min_value=0,format="%.2f")
            kg_pescado = st.number_input("Gramos de pescado", min_value=0,format="%.2f")
            huevos= st.number_input("Cantidad de huevos", min_value=0,format="%.2f")
            kg_leche = st.number_input("Litros de leche", min_value=0,format="%.2f")
            kg_queso = st.number_input("Gramos de queso", min_value=0,format="%.2f")
            kg_arroz = st.number_input("Gramos de arroz", min_value=0,format="%.2f")
            kg_pan = st.number_input("Gramos de pan", min_value=0,format="%.2f")
            kg_papa = st.number_input("Gramos de papa", min_value=0,format="%.2f")

    submitted = st.form_submit_button("Calcular")
    huella = calcula_huella(km_auto, km_moto, km_colect_die, hs_tele,hs_aire,hs_ventilador, hs_heladera,hs_lavarropa,hs_plancha,hs_horno_elect,hs_microondas, kg_carne_vaca, kg_carne_cerdo, kg_pollo, kg_pescado, huevos, kg_leche, kg_queso, kg_arroz, kg_pan, kg_papa)


if submitted:
    st.write(f"Tu huella de carbono SEMANAL es: :red[{round(huella,3)}] KgCO₂eq")
    st.write(f"Tu huella de carbono ANUAL es: :red[{round(huella*12,3)}] KgCO₂eq")

    impacto_arboles = obtener_impacto_arboles(huella)
    st.write(f"Esto equivale a la absorción de CO2 de aproximadamente :red[{round(impacto_arboles*12,3)}] árboles al año.")

    #st.write(f"Esto equivale a la absorción de CO2 de aproximadamente :red[{round(impacto_arboles,1)}] árboles.")

    st.write("**:blue[Algunas de las opciones que puedes considerar para bajar tu huella de carbono pueden ser:]**")
    for mensaje in obtener_compensacion_ejemplos():
       st.write(f"- {mensaje}")
    
    st.write("**:green[Recuerda que cada pequeña acción cuenta, y juntos podemos hacer la diferencia para reducir nuestra huella de carbono y contribuir a un futuro más sostenible.]**")
