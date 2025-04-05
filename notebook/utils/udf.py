import pandas as pd

PRICING = {
    "aws": {
        'cpu_per_milli': 0.0000012,    # ~$0.00432 USD/vCPU-hora
        'memory_per_mib': 0.0000004,   # ~$1.44 USD/GB-hora
        'gpu_base': 0.35,              # NVIDIA T4
        'gpu_per_milli': 0.00000035    # ~$1.26 USD/GPU-hora
    },
    "gcp": {
        'cpu_per_milli': 0.0000011,    # ~$0.00396 USD/vCPU-hora
        'memory_per_mib': 0.00000035,  # ~$1.26 USD/GB-hora
        'gpu_base': 0.30,              # NVIDIA T4
        'gpu_per_milli': 0.0000003     # ~$1.08 USD/GPU-hora
    },
    "azure": {
        'cpu_per_milli': 0.0000013,    # ~$0.00468 USD/vCPU-hora
        'memory_per_mib': 0.00000045,  # ~$1.62 USD/GB-hora
        'gpu_base': 0.40,              # NVIDIA T4
        'gpu_per_milli': 0.0000004     # ~$1.44 USD/GPU-hora
    }
}

def calculate_cloud_cost(row):
    cost_results = {}
    
    for provider in PRICING:
        # Precios del proveedor actual
        prices = PRICING[provider]
        
        # Cálculo de costos
        cpu_cost = row['cpu_milli'] * prices['cpu_per_milli']
        memory_cost = row['memory_mib'] * prices['memory_per_mib']
        gpu_cost = (row['num_gpu'] * prices['gpu_base']) + (row['gpu_milli'] * prices['gpu_per_milli'])
        
        # Costo total por hora
        total_cost = (cpu_cost + memory_cost + gpu_cost) * 3600
        
        # Almacenar resultados
        cost_results[f'cost_{provider}'] = round(total_cost, 2)
    
    return pd.Series(cost_results)  # Retorna una Serie para crear columnas en un DataFrame