# Odoomancy
**Odoomancy** es un conjunto de módulos desarrollados sobre Odoo orientado a la gestión de partidas de Dungeons & Dragons dentro de un entorno estructurado, persistente y extensible desarrollado por auténticas **Odoomantes**.

## Objetivo
El objetivo del proyecto es centralizar toda la información de una campaña y proporcionar una única herramienta adaptada para mejorar la experiencia de los jugadores y del Dungeon Master.

- **La Odoomancia** permitirá gestionar personajes, recursos y progreso de la campaña desde un único sistema, manteniendo la información organizada y accesible. Hojas de personaje desarrolladas en React, donde los jugadores pueden consultar y gestionar atributos, inventario, equipamiento y hechizos. Estas hojas interactivas consumen directamente los datos definidos en Odoo.
- En fases más avanzadas de **La Odoomancia**, se incorporará una visualización del progreso de la campaña mediante un timeline con ramificaciones, que permite representar decisiones y distintos caminos narrativos. El Dungeon Master puede intervenir sobre esta estructura de forma controlada.
- Corre el rumor de que algunos **Odoomantes** están trabajando en un gestor de combates que estructura encuentros mediante turnos, estados y acciones, integrándose con los personajes y entidades del **Sistema Odoomántico**. 

Además, existe un módulo independiente de importación que consume la API de DnD 5e para una carga inicial de datos.

## Arquitectura
El proyecto está dividido actualmente en tres módulos:
- Un módulo principal en Odoo que contiene los modelos y lógica de negocio: **Odoomancy**
- Un módulo de importación encargado de sincronizar datos desde la API externa: **Odoomancy data import**
- Un frontend en React orientado a los jugadores: **Odoomancy character sheet**

## Estado
El desarrollo se encuentra en curso, actualmente centrado en el modelado de datos, la importación desde la API y la base de las hojas de personaje. Para colaborar, dirigirse telemáticamente a cualquier **Odoomante** y esperar a recibir órdenes.

## Recursos
- API DnD 5e: https://www.dnd5eapi.co/api/2014
- Repositorio: https://github.com/JLandion/Odoomancy
