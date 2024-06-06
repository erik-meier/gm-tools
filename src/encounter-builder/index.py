from encounter import Difficulty

CR_PER_CHARACTER = {
        Difficulty.EASY: [
            0.125,
            0.125,
            0.25,
            0.5,
            1,
            1.5,
            2,
            2.5,
            3,
            3.5,
            4,
            4.5,
            5,
            5.5,
            6,
            6.5,
            7,
            7.5,
            8,
            8.5
        ],
        Difficulty.STANDARD: [
            0.125,
            0.25,
            0.5,
            0.75,
            1.5,
            2,
            2.5,
            3,
            3.5,
            4,
            4.5,
            5,
            5.5,
            6,
            6.5,
            7,
            7.5,
            8,
            8.5,
            9
        ],
        Difficulty.HARD: [
            0.25,
            0.5,
            0.75,
            1,
            2.5,
            3,
            3.5,
            4,
            4.5,
            5,
            5.5,
            6,
            6.5,
            7,
            7.5,
            8,
            8.5,
            9,
            9.5,
            10
        ]
    }

CAP_PER_LEVEL = [
        1,
        3,
        4,
        6,
        8,
        9,
        10,
        12,
        13,
        15,
        16,
        17,
        19,
        20,
        22,
        24,
        25,
        26,
        28,
        30
    ]

CAP_FOR_DIFFICULTY = {
    4: {
        Difficulty.TRIVIAL: "30,7",
        Difficulty.EASY: "6,5",
        Difficulty.STANDARD: "4,3",
        Difficulty.HARD: "2,0"
    },
    5: {
        Difficulty.TRIVIAL: "30,7",
        Difficulty.EASY: "6,5",
        Difficulty.STANDARD: "4,3",
        Difficulty.HARD: "2,0"
    },
    6: {
        Difficulty.TRIVIAL: "30,6",
        Difficulty.EASY: "5,4",
        Difficulty.STANDARD: "3,2",
        Difficulty.HARD: "1,0" 
    },
    7: {
        Difficulty.TRIVIAL: "30,6",
        Difficulty.EASY: "5,4",
        Difficulty.STANDARD: "3,2",
        Difficulty.HARD: "1,0" 
    }
}