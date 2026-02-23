from pathlib import Path
import os

def create_html_summary(folder_path, output_file='summary.html'):
    """
    Crée un fichier HTML résumant tous les fichiers HTML du dossier
    """
    folder = Path(folder_path)
    
    try:
        if not folder.exists():
            print(f"Erreur: Le dossier '{folder_path}' n'existe pas")
            return
            
        html_files = []
        
        # Collecte les fichiers HTML
        for file in folder.iterdir():
            if file.is_file() and file.suffix == '.html':
                html_files.append(file)
        
        # Génère le contenu HTML
        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Résumé des pages HTML</title>
    <link rel="stylesheet" href="summary.css">
</head>
<body>
    <h1>Résumé des pages HTML dans '{folder_path}'</h1>
    <p>Total: {len(html_files)} fichiers HTML</p>
    
    <div class="links-grid">
"""
        
        for file in html_files:
            stat = file.stat()
            size = stat.st_size
            size_str = f"{size} octets"
            
            html_content += f"""
        <a href="{file.name}" class="file-item">{file.name}</a>
"""
        
        html_content += """
    </div>
</body>
</html>
"""
        
        # Écrit le fichier de résumé
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"Résumé généré dans '{output_file}'")
        
    except Exception as e:
        print(f"Erreur: {e}")

# Utilisation
create_html_summary('', 'pages_summary.html')