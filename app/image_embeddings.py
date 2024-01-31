from transformers import ViTFeatureExtractor, ViTModel
from PIL import Image

def get_image_embeddings(image_path, model_name='google/vit-base-patch16-224'):
    feature_extractor = ViTFeatureExtractor.from_pretrained(model_name)
    model = ViTModel.from_pretrained(model_name)
    
    image = Image.open(image_path)
    inputs = feature_extractor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1)  # Mean pooling
    return embeddings
