import folium
from django.shortcuts import render
from .models import Question, Character
from .models import VerseCard
def menu_view(request):
    return render(request, "menu.html")
def verse_cards(request):
    cards = VerseCard.objects.all()
    return render(request, "verse_cards.html", {"cards": cards})

def quiz_view(request):
    # Traer todas las preguntas con sus opciones
    questions = Question.objects.prefetch_related("options").all()

    # Construir lista con cada pregunta y su opción correcta
    questions_with_correct = []
    for q in questions:
        correct_option = q.options.filter(is_correct=True).first()
        questions_with_correct.append({
            "id": q.id,
            "text": q.text,
            "options": q.options.all(),
            "correct_option_id": correct_option.id if correct_option else None
        })

    # Renderizar la plantilla que usa fichas y modales
    return render(request, "quiz.html", {
        "questions": questions_with_correct
    })


def memory_game(request): 
    characters = Character.objects.all() 
    return render(request, "memory_game.html", {"characters": characters})

# 👉 Nueva vista para el mapa
def map_view(request):
    mapa = folium.Map(location=[37.0, 15.0], zoom_start=5)

    ruta = [
        [36.2, 37.0],   # Antioquía de Siria
        [35.2, 33.0],   # Seleucia
        [35.2, 33.6],   # Salamina (Chipre)
        [34.8, 32.4],   # Pafos (Chipre)
        [37.0, 27.0],   # Perge (Panfilia)
        [37.9, 32.5],   # Antioquía de Pisidia
        [39.0, 34.0],   # Iconio
        [38.3, 33.2],   # Listra
        [37.6, 31.0],   # Derbe
    ]
    mapa = folium.Map(location=[37.0, 15.0], zoom_start=5, tiles="CartoDB positron") 
    # Tramo: Antioquía → Seleucia 
    folium.PolyLine([[36.2, 37.0], [35.2, 33.0]], color="blue", weight=3, opacity=0.8).add_to(mapa) 

    # Tramo: Seleucia → Salamina 
    folium.PolyLine([[35.2, 33.0], [35.2, 33.6]], color="red", weight=3, opacity=0.8).add_to(mapa) 

    # Tramo: Salamina → Pafos 
    folium.PolyLine([[35.2, 33.6], [34.8, 32.4]], color="green", weight=3, opacity=0.8).add_to(mapa) 

    # Tramo: Pafos → Perge 
    folium.PolyLine([[34.8, 32.4], [37.0, 27.0]], color="purple", weight=3, opacity=0.8).add_to(mapa) 

    # Tramo: Perge → Antioquía de Pisidia 
    folium.PolyLine([[37.0, 27.0], [37.9, 32.5]], color="orange", weight=3, opacity=0.8).add_to(mapa) 
    
    # Tramo: Antioquía de Pisidia → Iconio 
    folium.PolyLine([[37.9, 32.5], [39.0, 34.0]], color="brown", weight=3, opacity=0.8).add_to(mapa) 
    
    # Tramo: Iconio → Listra 
    folium.PolyLine([[39.0, 34.0], [38.3, 33.2]], color="pink", weight=3, opacity=0.8).add_to(mapa) 
    
    # Tramo: Listra → Derbe 
    folium.PolyLine([[38.3, 33.2], [37.6, 31.0]], color="cyan", weight=3, opacity=0.8).add_to(mapa)
    
    # Marcadores para cada ciudad 
    folium.Marker([36.2, 37.0], tooltip="Antioquía de Siria", 
                    popup="📖 Primera ciudad del viaje").add_to(mapa) 
    folium.Marker([35.2, 33.0], tooltip="Seleucia", 
                    popup="📖 Puerto de salida hacia Chipre").add_to(mapa) 
    folium.Marker([35.2, 33.6], tooltip="Salamina", 
                    popup="📖 Aquí predicaron en las sinagogas").add_to(mapa) 
    folium.Marker([34.8, 32.4], tooltip="Pafos", 
                    popup="📖 Encuentro con el procónsul Sergio Paulo").add_to(mapa) 
    folium.Marker([37.0, 27.0], tooltip="Perge", 
                    popup="📖 Juan Marcos se separa del grupo").add_to(mapa) 
    folium.Marker([37.9, 32.5], tooltip="Antioquía de Pisidia", 
                    popup="📖 Pablo predica en la sinagoga").add_to(mapa) 
    folium.Marker([39.0, 34.0], tooltip="Iconio", 
                    popup="📖 Muchos creyeron, pero hubo oposición").add_to(mapa) 
    folium.Marker([38.3, 33.2], tooltip="Listra", 
                    popup="📖 Pablo sana a un cojo y es confundido con un dios").add_to(mapa) 
    folium.Marker([37.6, 31.0], tooltip="Derbe", 
                    popup="📖 Última ciudad del viaje antes de regresar").add_to(mapa)

    folium.Marker(
        location=[36.1699, 14.0],
        popup=folium.Popup("📖 Pregunta: ¿Cuál fue la primera ciudad donde Pablo y Bernabé predicaron en su primer viaje misionero?", max_width=300),
        tooltip="Antioquía de Siria"
    ).add_to(mapa)
    
    # Renderizar el mapa como HTML
    mapa_html = mapa._repr_html_()

    return render(request, "mapa.html", {"mapa": mapa_html})
