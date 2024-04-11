import models
user_reviews = [
    "Improved durability for long-term use.",
    "Integration with other devices for increased functionality.",
    "Customizable settings to tailor the product to individual preferences.",
    "Option for eco-friendly materials and manufacturing processes.",
    "Compatibility with third-party accessories for expanded capabilities.",
    "Improved packaging to reduce environmental impact.",
    "Option for wireless connectivity for added convenience.",
    "Inclusion of a user manual with detailed instructions.",
    "This product is amazing! It exceeded all of my expectations.",
    "I'm really impressed with the quality of this product.",
    "Great value for the price. Definitely worth it.",
    "I love this product! It's exactly what I needed.",
    "Highly recommend this product to anyone in need.",
    "Not happy with this purchase. It broke after only a few uses.",
    "The product arrived damaged. Very disappointed.",
    "Terrible quality. I regret buying it.",
    "I'm disappointed with the performance of this product.",
    "I wish I hadn't wasted my money on this product.",
    "This product is flimsy and cheaply made.",
    "I had high hopes for this product but I was let down.",
    "The product arrived missing parts. Not impressed.",
    "I'm extremely disappointed with the quality of this product.",
    "The product stopped working after only a few days.",
    "I've had nothing but problems with this product since day one.",
    "This product is overpriced for what you get.",
    "I'm disappointed with the lack of features in this product.",
    "The product didn't meet my expectations at all.",
     "I received compliments on this product from everyone who saw it.",
    "I'm not sure how I ever lived without this product.",
    "I'm blown away by how great this product is.",
    "I've already bought multiple of these products because I love them so much.",
    "I'm amazed by the results I've seen from using this product.",
    "I'm very impressed with the customer service I received.",
    "I've already recommended this product to all of my friends.",
    "I'm impressed with how well this product works.",
    "It would be great to have a longer battery life.",
    "Adding a feature for automatic updates would be convenient.",
    "An option for voice commands would enhance usability.",
    "Including a carrying case for portability would be useful.",
    "Integration with popular apps like [specific app names] would be beneficial.",
    "Adding a built-in sensor for [specific function] would improve functionality.",
    "Including more preset modes for different use cases would be helpful.",
    "Adding support for multiple user profiles would be a great addition.",
    "Including a warranty extension option would provide peace of mind for users.",
    "It would be helpful to have a dedicated app for remote control and monitoring.",
    "Adding compatibility with virtual assistants like Alexa or Google Assistant would be great."
]


def callModel(title):
    chunk_size = 10
    review_chunks = [user_reviews[i:i + chunk_size] for i in range(0, len(user_reviews), chunk_size)]
    res=[]

    
    for chunk in review_chunks:
        template=f"You are a experienced in searching the user comments  to find for  {title} once  : i will give you few commnets you have to find them if found then give me the output as  array in javascript if it is not related to the [good] ignore it, the commnets are {chunk}  and dont give me the ```javascript in the resopnse"

        res =res + eval(models.gemini_pro_test(template))   
        
    return res

