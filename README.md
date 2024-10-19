<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <h1>README - [Proyecto Final Informatorio - Blog con Django]</h1>
</head>
<div>
    <a href="https://github.com/Casullo/FINAL_PRO/branches" target="_blank">
        <img alt="Static Badge" src="https://img.shields.io/badge/Ramas_Creadas-repo_final-blue?style=social&link=https%3A%2F%2Fgithub.com%2FCasullo%2FFINAL_PRO%2Fbranches">
    </a>
</div>
<body>
    <h2>Descripción</h2>
    <p>Para la versión mínima del proyecto, se solicita que se incluyan las siguientes funcionalidades:</p>
  <d1>
        <dt>▶ El acceso de diversos perfiles (admin, registrado, etc).<dt>
        <dt>▶ Cargar un nuevo post, eliminar post publicados (con diversas restricciones).</dt>
        <dt>▶ Comentar posts por parte de usuarios con perfil registrado. Un usuario debe estar autenticado y tener perfil registrado para poder comentar. </dt>
        <dt>▶ Login a usuario tipo admin y registrado.</dt>
        <dt>▶ Filtrar post por fecha, categoría de post y comentarios recibidos.</dt>
    </d1>
    <h2>Instrucciones de Instalación</h2>
    <ol>
        <li><strong>Clonar el repositorio</strong>
            <pre><code>git clone -b master https://github.com/usuario/repositorio.git</code></pre></li>
  <li><strong>Crear entorno Virtual</strong></li>
  <li><strong>Instalar dependencias de requirements.txt</strong></li>
      <pre><code>python -m pip install requirements.txt</code></pre>
      <li><strong>Crear local.py en blog/blog/configuraciones</strong></li>
      <p>En este archivo se importan todas las configuraciones de settings.py</p>
      <p>agregando esta linea al alrchivo</p>
      <pre><code>from .settings import *</code></pre>
    </ol>
    <h2>Enlaces Útiles</h2>
    <ul>
        <li><a href="https://trello.com/invite/b/66e60fea32b2afaa85c8d813/ATTIbcfa5428efcc4202bbba1f19393e00a9DF5E8464/proyecto-final-grupo-2-comi-5">Trello</a>: Organización del equipo.</li>
        <li><a href="https://www.figma.com/design/XFB2EEGldFwfuwshqq2IZw/PROYECTO-FINAL?node-id=0-1&t=nFI6KJq4wJv3pd7X-1">Figma</a>: Diseño visual de la aplicación.</li>
        <li><a href="https://drive.google.com/file/d/1jFNxLm-oQZ_m4YIyr-qxQcYB-ZWW4eV3/view?usp=drive_link">Draw.io</a>: Modelado entidad-relación de las bases de datos.</li>
    </ul>
    <h2>Miembros del Equipo (Comisión 5, Grupo 2)</h2>
    <ul>
        <li><strong>Nazzer Hiemur</strong> - <a href="https://github.com/nazhiemur">GitHub</a> | <a href="#">LinkedIn</a></li>
        <li><strong>Martin Vernazza</strong> - <a href="https://github.com/martinvernazza42">GitHub</a> | <a href="#">LinkedIn</a></li>
        <li><strong>Matias Alvares</strong> - <a href="https://github.com/AlvMati">GitHub</a> | <a href="#">LinkedIn</a></li>
        <li><strong>Sebastian Casullo</strong> - <a href="https://github.com/Casullo">GitHub</a> | <a href="#">LinkedIn</a></li>
        <li><strong>Gabriel Pokorasky</strong> - <a href="https://github.com/GabiPoko">GitHub</a> | <a href="#">LinkedIn</a></li>
    </ul>
</body>
</html>
