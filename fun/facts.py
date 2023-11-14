import random

facts = {
    "history":[
        "The Great Wall of China, which stretches over 13,000 miles, was not built by a single emperor but was constructed by multiple Chinese dynasties over centuries.",
        "The American Revolution began in 1775 with the Battles of Lexington and Concord.",
        "The Egyptian pharaoh Cleopatra was the last ruler of the Ptolemaic Kingdom and had relationships with both Julius Caesar and Mark Antony.",
        "The Industrial Revolution, a period of rapid industrialization and technological advancements, began in the late 18th century in Great Britain.",
        "The signing of the Treaty of Versailles in 1919 officially ended World War I and imposed significant penalties on Germany."
    ],
    "scitech":[
        "The first computer programmer was Ada Lovelace, who wrote algorithms for Charles Babbage's early mechanical general-purpose computer.",
        "The speed of light in a vacuum is approximately 299,792,458 meters per second (about 186,282 miles per second).",
        "The periodic table of elements was created by Dmitri Mendeleev in 1869, who organized elements by their atomic number and properties.",
        "The first successful human heart transplant was performed by Dr. Christiaan Barnard in South Africa in 1967.",
        "The Hubble Space Telescope, launched in 1990, has provided remarkable images and insights into the universe."
    ],
    "geo":[
        "The Hubble Space Telescope, launched in 1990, has provided remarkable images and insights into the universe.",
        "The Sahara Desert in North Africa is the largest hot desert in the world, covering over 3.6 million square miles.",
        "The Great Barrier Reef in Australia is the world's largest coral reef system and is visible from space.",
        "Mount Everest, standing at 29,032 feet (8,849 meters) above sea level, is the highest peak on Earth.",
        "The Dead Sea, located between Israel and Jordan, is one of the saltiest bodies of water in the world, with a salt concentration so high that people easily float on its surface."
    ],
    "famous":[
        "Albert Einstein, known for his theory of relativity, was awarded the Nobel Prize in Physics in 1921 for his work on the photoelectric effect.",
        "Nelson Mandela, the South African anti-apartheid revolutionary, became the country's first black president in 1994 after being released from prison.",
        "Marie Curie was the first person to win Nobel Prizes in two different scientific fields—Physics and Chemistry—for her work on radioactivity.",
        "Mahatma Gandhi, a leader of the Indian independence movement, practiced nonviolent civil disobedience to achieve political and social change.",
        "Leonardo da Vinci, a polymath of the Renaissance, is known for his contributions to art, science, and invention, including the Mona Lisa and designs for various machines."
    ],
    "health":[
        "The human body is composed of about 37.2 trillion cells, each with a specific function.",
        "The recommended daily intake of water for an average adult is about 8 cups, or 64 ounces.",
        "The concept of handwashing to prevent the spread of diseases was popularized by Dr. Ignaz Semmelweis in the 19th century.",
        "Regular physical activity is associated with a reduced risk of chronic health conditions, such as heart disease and diabetes.",
        "The discovery of antibiotics by Alexander Fleming in 1928 revolutionized medicine by enabling the treatment of bacterial infections."
    ]
}


def fun(query: str) -> str:
    return random.choice(facts[query])