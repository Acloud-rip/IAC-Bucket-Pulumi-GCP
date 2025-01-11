import pulumi
import pulumi_gcp as gcp

# Configuración del proyecto de GCP
config = pulumi.Config()
project_id = config.require('gcp_project_id')
region = config.get('region', 'us-central1')

# Crear un bucket de GCS
bucket = gcp.storage.Bucket('mi-bucket-proyecto', 
    project=project_id,
    location=region,
    force_destroy=True,  # Permite eliminar el bucket incluso si contiene objetos
    uniform_bucket_level_access=True,  # Mejora la seguridad
    storage_class='STANDARD',
    
    # Configuraciones de seguridad y versionado
    versioning={
        'enabled': True
    },
    
    # Política de eliminación de objetos antiguos (opcional)
    lifecycle_rules=[{
        'action': {
            'type': 'Delete'
        },
        'condition': {
            'age': 365  # Eliminar objetos después de un año
        }
    }]
)

# Exportar el nombre del bucket
pulumi.export('bucket_name', bucket.name)