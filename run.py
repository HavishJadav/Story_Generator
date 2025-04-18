from story_generator.generator import StoryGenerator

def main():
    prompt = input("Enter a story prompt: ")
    generator = StoryGenerator()
    story = generator.generate(prompt)
    
    print("\nGenerated Story:\n")
    print(story)

if __name__ == "__main__":
    main()
