from utils import create_input_files

if __name__ == '__main__':
    # Create input files (along with word map)
    create_input_files(dataset='coco',
                       karpathy_json_path='F:\\IMAGE_CAPTIONING\\I_CAP\\caption_datasets\\dataset_coco.json',
                       image_folder='F:\\IMAGE_CAPTIONING\\I_CAP\\dataset\\',
                       captions_per_image=5,
                       min_word_freq=5,
                       output_folder='F:\\IMAGE_CAPTIONING\\I_CAP\\output\\',
                       max_len=50)
