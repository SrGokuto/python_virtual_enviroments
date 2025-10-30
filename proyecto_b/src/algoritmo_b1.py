import pandas as pd
import numpy as np

# Create a sample dataset
def create_sample_data():
    """Create a sample dataset with sales information"""
    data = {
        'producto': ['Laptop', 'Mouse', 'Teclado', 'Monitor', 'Laptop', 
                     'Mouse', 'Teclado', 'Monitor', 'Laptop', 'Mouse'],
        'categoria': ['Electrónica', 'Accesorios', 'Accesorios', 'Electrónica', 
                      'Electrónica', 'Accesorios', 'Accesorios', 'Electrónica',
                      'Electrónica', 'Accesorios'],
        'ventas': [1200, 25, 45, 300, 1100, 30, 50, 280, 1300, 28],
        'cantidad': [2, 10, 5, 3, 1, 12, 6, 2, 3, 8],
        'region': ['Norte', 'Sur', 'Este', 'Oeste', 'Norte', 
                   'Sur', 'Este', 'Oeste', 'Norte', 'Sur']
    }
    return pd.DataFrame(data)

def analyze_sales(df):
    """Perform various analyses on the sales data"""
    print("=" * 60)
    print("ANÁLISIS DE VENTAS")
    print("=" * 60)
    
    # 1. Show basic information
    print("\n1. Primeras filas del dataset:")
    print(df.head())
    
    # 2. Basic statistics
    print("\n2. Estadísticas descriptivas:")
    print(df.describe())
    
    # 3. Filter products with sales > 100
    print("\n3. Productos con ventas mayores a 100:")
    high_sales = df[df['ventas'] > 100]
    print(high_sales)
    
    # 4. Group by category and calculate totals
    print("\n4. Ventas totales por categoría:")
    category_sales = df.groupby('categoria')['ventas'].sum().sort_values(ascending=False)
    print(category_sales)
    
    # 5. Group by product and calculate average
    print("\n5. Promedio de ventas por producto:")
    product_avg = df.groupby('producto').agg({
        'ventas': 'mean',
        'cantidad': 'sum'
    }).round(2)
    print(product_avg)
    
    # 6. Add a new column with total revenue
    df['ingreso_total'] = df['ventas'] * df['cantidad']
    print("\n6. Dataset con columna de ingreso total:")
    print(df[['producto', 'ventas', 'cantidad', 'ingreso_total']])
    
    # 7. Find top selling region
    print("\n7. Ventas totales por región:")
    region_sales = df.groupby('region')['ingreso_total'].sum().sort_values(ascending=False)
    print(region_sales)
    print(f"\nMejor región: {region_sales.idxmax()} con ${region_sales.max():,.2f}")
    
    return df

def main():
    """Main function to run the algorithm"""
    # Create the dataset
    df = create_sample_data()
    
    # Perform analysis
    df_analyzed = analyze_sales(df)
    
    # Export to CSV (optional)
    output_file = './analisis_ventas.csv'
    df_analyzed.to_csv(output_file, index=False)
    print(f"\n{'=' * 60}")
    print(f"Análisis guardado en: {output_file}")
    print("=" * 60)

if __name__ == "__main__":
    main()
