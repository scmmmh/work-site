import subprocess


def task_build_css():
    def run():
        sass_result = subprocess.run(['sass', '--load-path', 'node_modules/foundation-sites/scss', 'theme/src/app.scss'], capture_output=True)
        postcss_result = subprocess.run(['postcss', '--use', 'autoprefixer', '--no-map'], input=sass_result.stdout, capture_output=True)
        with open('theme/static/css/app.css', 'wb') as out_f:
            out_f.write(postcss_result.stdout)

    return {
        'actions': [run],
        'file_dep': ['theme/src/app.scss'],
    }
