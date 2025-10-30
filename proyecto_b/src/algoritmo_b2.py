import pandas as pd
import os

def load_student_data(filename):
    """Load student data from CSV file"""
    if not os.path.exists(filename):
        print(f"Error: El archivo {filename} no existe.")
        return None
    
    try:
        df = pd.read_csv(filename)
        print(f"✓ Datos cargados exitosamente desde {filename}")
        print(f"  Total de registros: {len(df)}")
        return df
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return None

def analyze_students(df):
    """Perform comprehensive analysis on student data"""
    print("\n" + "=" * 70)
    print("ANÁLISIS DE DATOS DE ESTUDIANTES")
    print("=" * 70)
    
    # 1. Display basic information
    print("\n1. Información del dataset:")
    print(f"   - Número de estudiantes: {len(df)}")
    print(f"   - Columnas: {', '.join(df.columns.tolist())}")
    
    # 2. Show first rows
    print("\n2. Primeras 5 filas del dataset:")
    print(df.head())
    
    # 3. Basic statistics
    print("\n3. Estadísticas descriptivas:")
    print(df.describe())
    
    # 4. Students by major
    print("\n4. Distribución de estudiantes por carrera:")
    carrera_count = df['carrera'].value_counts()
    print(carrera_count)
    
    # 5. Average grade by major
    print("\n5. Promedio de calificaciones por carrera:")
    promedio_carrera = df.groupby('carrera')['promedio'].agg(['mean', 'min', 'max']).round(2)
    promedio_carrera.columns = ['Promedio', 'Mínimo', 'Máximo']
    print(promedio_carrera)
    
    # 6. Students by city
    print("\n6. Estudiantes por ciudad:")
    ciudad_count = df.groupby('ciudad').size().sort_values(ascending=False)
    print(ciudad_count)
    
    # 7. Filter high-performing students (grade >= 9.0)
    print("\n7. Estudiantes con promedio ≥ 9.0:")
    top_students = df[df['promedio'] >= 9.0][['nombre', 'carrera', 'promedio']].sort_values('promedio', ascending=False)
    print(top_students)
    
    # 8. Average age by semester
    print("\n8. Edad promedio por semestre:")
    edad_semestre = df.groupby('semestre')['edad'].mean().round(1)
    print(edad_semestre)
    
    # 9. Add performance category
    def categorize_performance(grade):
        if grade >= 9.0:
            return 'Excelente'
        elif grade >= 8.0:
            return 'Bueno'
        elif grade >= 7.0:
            return 'Regular'
        else:
            return 'Necesita mejorar'
    
    df['categoria_rendimiento'] = df['promedio'].apply(categorize_performance)
    
    print("\n9. Distribución por categoría de rendimiento:")
    rendimiento_dist = df['categoria_rendimiento'].value_counts()
    print(rendimiento_dist)
    
    # 10. Top 5 students overall
    print("\n10. Top 5 estudiantes con mejor promedio:")
    top_5 = df.nlargest(5, 'promedio')[['nombre', 'carrera', 'promedio', 'ciudad']]
    print(top_5.to_string(index=False))
    
    return df

def generate_report(df, output_filename):
    """Generate a summary report and save to CSV"""
    print("\n" + "=" * 70)
    print("GENERANDO REPORTE")
    print("=" * 70)
    
    # Create summary by major and city
    summary = df.groupby(['carrera', 'ciudad']).agg({
        'nombre': 'count',
        'promedio': 'mean',
        'edad': 'mean'
    }).round(2)
    
    summary.columns = ['total_estudiantes', 'promedio_calificacion', 'edad_promedio']
    summary = summary.reset_index()
    
    # Save to CSV
    summary.to_csv(output_filename, index=False)
    print(f"\n✓ Reporte guardado en: {output_filename}")
    print("\nContenido del reporte:")
    print(summary)
    
    return summary

def main():
    """Main function to run the algorithm"""
    # Input and output files
    input_file = './src/estudiantes.csv'
    output_file = 'reporte_estudiantes.csv'
    
    # Load data
    df = load_student_data(input_file)
    
    if df is not None:
        # Analyze data
        df_analyzed = analyze_students(df)
        
        # Generate report
        generate_report(df_analyzed, output_file)
        
        print("\n" + "=" * 70)
        print("ANÁLISIS COMPLETADO")
        print("=" * 70)

if __name__ == "__main__":
    main()
