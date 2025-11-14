from app import create_app
from models import db, Question, User

# MCQ data for different roles
MCQ_DATA = {
    "Cleaner": [
        {
            'question_text': 'How should the work area be made safe while cleaning? (px7m2k1n)',
            'option_a': 'Do not inform anyone',
            'option_b': 'Place a sign like "Wet Floor" or "Cleaning in Progress"',
            'option_c': 'Work quietly',
            'option_d': 'Only sweep the floor',
            'correct_option': 'B'
        },
        {
            'question_text': 'How should different cleaning chemicals be used? (rx3n8l4p)',
            'option_a': 'Use without instruction',
            'option_b': 'Use according to company instructions',
            'option_c': 'Use as you wish',
            'option_d': 'Mix to make them stronger',
            'correct_option': 'B'
        },
        {
            'question_text': 'What material is used to clean glass? (jx9v5k2m)',
            'option_a': 'Floor cleaner',
            'option_b': 'Glass cleaner and soft cloth',
            'option_c': 'Water and broom',
            'option_d': 'Bleach',
            'correct_option': 'B'
        },
        {
            'question_text': 'When should cleaning tools be cleaned? (nx1r6j8t)',
            'option_a': 'Once a week',
            'option_b': 'After every use',
            'option_c': 'Only when dirty',
            'option_d': 'Never',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should a cleaner pay special attention to? (tw4m9l3u)',
            'option_a': 'Time, cleanliness, and safety',
            'option_b': 'Only supervisor\'s words',
            'option_c': 'Rest',
            'option_d': 'Interfering in others\' work',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is important for cleaning different areas? (qx7n5k1j)',
            'option_a': 'Use the same cloth everywhere',
            'option_b': 'Use a separate cloth or mop for each area',
            'option_c': 'Clean everything with water',
            'option_d': 'Use one broom for all',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should you do if a guest or client is not satisfied with the cleaning? (sx2p8m5r)',
            'option_a': 'Ignore them',
            'option_b': 'Apologize and clean better',
            'option_c': 'Argue with them',
            'option_d': 'Stay silent',
            'correct_option': 'B'
        },
        {
            'question_text': 'During kitchen cleaning, what is most important? (lx4t9n2k)',
            'option_a': 'Clean only the floor',
            'option_b': 'Remove all oil and grease completely',
            'option_c': 'Eat food',
            'option_d': 'Wash only dishes',
            'correct_option': 'B'
        },
        {
            'question_text': 'If there is a risk of electric shock in any area, what should be done? (mx6j1p5l)',
            'option_a': 'Pour water',
            'option_b': 'Inform the supervisor or electrician immediately',
            'option_c': 'Continue cleaning',
            'option_d': 'Do nothing',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should a cleaner do when working in a team? (rx8k3m7n)',
            'option_a': 'Argue',
            'option_b': 'Help each other',
            'option_c': 'Work alone',
            'option_d': 'Blame others',
            'correct_option': 'B'
        },
        {
            'question_text': 'Why are you suitable for a cleaner’s job? (tw9k5j2m)',
            'option_a': 'Because I am honest, punctual, and tidy',
            'option_b': 'Because I am free',
            'option_c': 'Because my friends told me',
            'option_d': 'Just trying for luck',
            'correct_option': 'A'
        },
        {
            'question_text': 'When using disinfectant to kill germs, what should be done? (ox4t7n1p)',
            'option_a': 'Use in large quantity',
            'option_b': 'Mix and use according to instructions',
            'option_c': 'Use without gloves',
            'option_d': 'Apply without water',
            'correct_option': 'B'
        },
        {
            'question_text': 'Why is “System Colour Coding” used in cleaning? (tw6m8j3r)',
            'option_a': 'To identify cleaning cloths for each area',
            'option_b': 'Because colours look nice',
            'option_c': 'To save time',
            'option_d': 'For supervisor only',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the difference between “Sanitizing” and “Disinfecting”? (rx5k9l2t)',
            'option_a': 'Both are the same',
            'option_b': 'Sanitizing removes dirt, Disinfecting kills germs',
            'option_c': 'Sanitizing kills germs',
            'option_d': 'Disinfecting cleans cloths',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the purpose of a “Material Safety Data Sheet (MSDS)”? (ox7n4j1m)',
            'option_a': 'To show the company name',
            'option_b': 'To give safety information for using cleaning chemicals',
            'option_c': 'To keep a record of cleaners',
            'option_d': 'To know salary details',
            'correct_option': 'B'
        },
        {
            'question_text': 'In hospital cleaning, what needs the most care? (rx2k8p5n)',
            'option_a': 'Cleaning only the floor',
            'option_b': 'Handling germs and bio-waste',
            'option_c': 'Talking to patients',
            'option_d': 'Cleaning quickly',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should a cleaner do if there is hazardous waste in an area? (jx9t3m7l)',
            'option_a': 'Pick it up by hand',
            'option_b': 'Wear proper PPE (safety gear) and inform supervisor',
            'option_c': 'Ignore it',
            'option_d': 'Clean it quickly',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should be done if a slip or fall accident happens during cleaning? (rx6k1n4p)',
            'option_a': 'Hide it',
            'option_b': 'Report immediately and give first aid',
            'option_c': 'Continue working',
            'option_d': 'Blame someone',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the most important quality of a professional cleaner? (ox8j2t5m)',
            'option_a': 'Cleaning speed',
            'option_b': 'Safety, honesty, and teamwork',
            'option_c': 'Focus on salary',
            'option_d': 'Work only in limited areas',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should a cleaner do after finishing daily duty? (tw5k9j1r)',
            'option_a': 'Keep all tools in proper place and report to supervisor',
            'option_b': 'Go home directly',
            'option_c': 'Chat with others',
            'option_d': 'Leave without informing',
            'correct_option': 'A'
        },
    ],

    'Carpenter': [
        {
            'question_text': 'What is meant by "A detailed drawing of the structure"? (nx4j8k2m)',
            'option_a': 'Engineer drawing',
            'option_b': 'Technical and detailed drawing',
            'option_c': 'Random drawing',
            'option_d': 'Rough sketch',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is a linear load? (wxj3mny0)',
            'option_a': 'Column',
            'option_b': 'Double panel (linear load)',
            'option_c': 'Plaster',
            'option_d': 'Rafter',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the purpose of applying oil in formwork? (rx6m9l3t)',
            'option_a': 'For minor work',
            'option_b': 'To prevent sticking of concrete to the formwork',
            'option_c': 'For drawing only',
            'option_d': 'For leveling',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the main function of a detailed shuttering? (tw8k4j7n)',
            'option_a': 'To maintain maximum concrete thickness',
            'option_b': 'To ensure proper curing',
            'option_c': 'Rough sketch',
            'option_d': 'Any random layout',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is a "Soffit" in formwork? (tw5j9k2m)',
            'option_a': 'Bottom face of the slab',
            'option_b': 'Slab surface',
            'option_c': 'Top of the slab',
            'option_d': 'Column top',
            'correct_option': 'A'
        },
        {
            'question_text': 'What should be done if props fail in formwork? (tw9k5j7n)',
            'option_a': 'Provide additional support immediately',
            'option_b': 'Wait and continue',
            'option_c': 'Ignore it',
            'option_d': 'Use hammer',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is a "Column Box"? (nx8m2l9k)',
            'option_a': 'Base of the column',
            'option_b': 'Vertical shuttering for a column',
            'option_c': 'Horizontal slab formwork',
            'option_d': 'Wall formwork',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is meant by "Props" or "Supports" in formwork? (nx7j4k8m)',
            'option_a': 'Temporary support',
            'option_b': 'Vertical support for structure',
            'option_c': 'Horizontal support',
            'option_d': 'Random timber',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is important for "Beam Bottom"? (tw2m6j9l)',
            'option_a': 'Proper alignment and spacing',
            'option_b': 'Engineer drawing',
            'option_c': 'Rough sketch',
            'option_d': 'Column layout',
            'correct_option': 'A'
        },
        {
            'question_text': 'What should be the thickness of shuttering plywood? (nx4j7k1m)',
            'option_a': '5 mm',
            'option_b': '12–18 mm',
            'option_c': '25 mm',
            'option_d': '3 mm',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the standard spacing of props for slab formwork? (tw4m9j3k)',
            'option_a': '24–48 inches',
            'option_b': 'Any random spacing',
            'option_c': 'Depends on floor area',
            'option_d': 'As desired',
            'correct_option': 'A'
        },
        {
            'question_text': 'How should vertical shuttering be supported? (tw6k8j2n)',
            'option_a': 'With proper props',
            'option_b': 'With rough timber',
            'option_c': 'Random placement',
            'option_d': 'As desired',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is “Nail spacing” in shuttering? (xxu0w694)',
            'option_a': 'Random placement',
            'option_b': 'As per design and alignment',
            'option_c': 'Any fixed length',
            'option_d': 'Column spacing',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the function of a "Tie Rod"? (tw2j8k5m)',
            'option_a': 'To hold vertical props together',
            'option_b': 'To support horizontal shuttering',
            'option_c': 'Temporary clamp',
            'option_d': 'Nail',
            'correct_option': 'A'
        },
        {
            'question_text': 'What are "Wedges" used for in formwork? (iwypk4fk)',
            'option_a': 'To adjust and fix alignment',
            'option_b': 'For decorative purpose',
            'option_c': 'For nailing',
            'option_d': 'Random timber',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is important in shuttering leveling? (lwmszqtt)',
            'option_a': 'Proper level and alignment',
            'option_b': 'Random placement',
            'option_c': 'Rough adjustment',
            'option_d': 'Use of nails',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is “Shuttering Oil” used for? (oxr8zj66)',
            'option_a': 'Water',
            'option_b': 'Diesel or mineral oil',
            'option_c': 'Paint',
            'option_d': 'Grease',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the purpose of props in shuttering? (mw12s1x9)',
            'option_a': 'To prevent collapse of formwork',
            'option_b': 'Random placement',
            'option_c': 'To adjust the height',
            'option_d': 'Decoration',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is meant by "Decking" in formwork? (nwe9q1ki)',
            'option_a': 'Floor slab formwork',
            'option_b': 'Random board',
            'option_c': 'Column top',
            'option_d': 'Wall shuttering',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the function of slab props? (vw3e4to9)',
            'option_a': 'To support slab load',
            'option_b': 'To support timber only',
            'option_c': 'Decoration',
            'option_d': 'For nails only',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is "Camber" in formwork? (qw96m5p6)',
            'option_a': 'Slight upward curve to counter slab deflection',
            'option_b': 'Random curvature',
            'option_c': 'Any slope',
            'option_d': 'Horizontal leveling',
            'correct_option': 'A'
        },
        {
            'question_text': 'What causes "Formwork Failure"? (gwsyy0m1)',
            'option_a': 'Improper tying of props and weak support',
            'option_b': 'Poor alignment',
            'option_c': 'Improper spacing',
            'option_d': 'Weak nails',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is "Centering"? (pxfi90l6)',
            'option_a': 'Random timber placement',
            'option_b': 'Correct placement of props and shuttering',
            'option_c': 'Slab reinforcement',
            'option_d': 'Column shuttering',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should be done after removing shuttering? (sw68oumy)',
            'option_a': 'Cure the concrete properly',
            'option_b': 'Remove rough work',
            'option_c': 'Leave as is',
            'option_d': 'Engineer inspection only',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is a basic tool for shuttering work? (gzlw2j84)',
            'option_a': 'Tape measure',
            'option_b': 'Hammer',
            'option_c': 'Saw',
            'option_d': 'Spirit level',
            'correct_option': 'D'
        },
        {
            'question_text': 'What is used for measuring and leveling in shuttering? (ew90zvxx)',
            'option_a': 'Measuring tape and spirit level',
            'option_b': 'Hammer',
            'option_c': 'Saw',
            'option_d': 'Chisel',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is a “Bevel”? (ewl66rxr)',
            'option_a': 'Angle of the timber',
            'option_b': 'Random cut',
            'option_c': 'Horizontal cut',
            'option_d': 'Vertical cut',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is a "Form Tie Hole"? (qwtm071g)',
            'option_a': 'Filled with wooden plug and cement paste',
            'option_b': 'Left empty',
            'option_c': 'Filled with resin',
            'option_d': 'Plastic plug',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the purpose of props under shuttering? (iw90772m)',
            'option_a': 'To support concrete load',
            'option_b': 'To support timber only',
            'option_c': 'Decoration',
            'option_d': 'Ignore',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is an “H-Beam” formwork used for? (uwww4n0h)',
            'option_a': 'Heavy slab and bridge construction',
            'option_b': 'Wall formwork',
            'option_c': 'Column formwork',
            'option_d': 'Beam only',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is meant by “Alignment” in formwork? (iw17x2q3)',
            'option_a': 'Proper positioning and layout',
            'option_b': 'Random positioning',
            'option_c': 'Rough placement',
            'option_d': 'Decoration',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is used to fix props in formwork? (zwlgji2n)',
            'option_a': 'Tie rods and clamps',
            'option_b': 'Nails only',
            'option_c': 'Timber only',
            'option_d': 'Hammer',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is a beam shuttering used for? (gw13i7o0)',
            'option_a': 'Support for concrete in beam',
            'option_b': 'Column shuttering',
            'option_c': 'Random timber',
            'option_d': 'Decoration',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the common material for bottom shuttering? (hxs2m3p3)',
            'option_a': 'Hardwood plywood',
            'option_b': 'Softwood',
            'option_c': 'Bamboo',
            'option_d': 'None',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the process after removing shuttering? (wx2vwyj4)',
            'option_a': 'Curing (keep concrete moist)',
            'option_b': 'Random adjustment',
            'option_c': 'Engineer inspection',
            'option_d': 'Ignore',
            'correct_option': 'B'
        },
    ],

    'Cashier': [
        {
            'question_text': 'What is the primary duty of a cashier? (nx2ztx0g)',
            'option_a': 'Talking to customers',
            'option_b': 'Correctly receiving and returning money',
            'option_c': 'Cleaning the store',
            'option_d': 'Packing orders',
            'correct_option': 'B'
        },
        {
            'question_text': 'What does POS stand for? (vwhl46hy)',
            'option_a': 'Point of Sale',
            'option_b': 'Power of System',
            'option_c': 'Print on Screen',
            'option_d': 'Pay or Sell',
            'correct_option': 'A'
        },
        {
            'question_text': 'What should you do if a customer is given the wrong change? (vx4u5ox2)',
            'option_a': 'Ignore it',
            'option_b': 'Check and give the correct amount immediately',
            'option_c': 'Argue with the customer',
            'option_d': 'Do not inform the manager',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the purpose of a receipt? (qxvoj0t5)',
            'option_a': 'To advertise',
            'option_b': 'To provide proof of purchase',
            'option_c': 'To increase the bill',
            'option_d': 'To hide information',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should a cashier do if the POS system is not working? (px8957l7)',
            'option_a': 'Make the customer wait',
            'option_b': 'Prepare a manual bill and inform the manager',
            'option_c': 'Close the store',
            'option_d': 'Refuse the customer',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the best method for counting cash? (ux65tg7z)',
            'option_a': 'Count quickly',
            'option_b': 'Count twice for accuracy',
            'option_c': 'Ask someone else to count',
            'option_d': 'Estimate the total',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should you do if a note looks suspicious? (exn90j6z)',
            'option_a': 'Keep it',
            'option_b': 'Show it to the manager or supervisor immediately',
            'option_c': 'Argue with the customer',
            'option_d': 'Destroy the note',
            'correct_option': 'B'
        },
        {
            'question_text': 'When is cash reconciliation done? (pwj8tyeu)',
            'option_a': 'At the end of the shift',
            'option_b': 'At the start of the day',
            'option_c': 'Once a week',
            'option_d': 'Whenever convenient',
            'correct_option': 'A'
        },
        {
            'question_text': 'What should a cashier do if a customer wants to pay by card? (fxxyxl3r)',
            'option_a': 'Refuse the card',
            'option_b': 'Complete the transaction using the card machine',
            'option_c': 'Ask for cash instead',
            'option_d': 'Call the manager',
            'correct_option': 'B'
        },
        {
            'question_text': 'When is it necessary for a cashier to sign a receipt? (uyyv13g8)',
            'option_a': 'Only for large bills',
            'option_b': 'When the customer requests',
            'option_c': 'According to company policy where signatures are required',
            'option_d': 'Never',
            'correct_option': 'C'
        },
        {
            'question_text': 'Which skill is most important for a cashier? (nxe9k2q4)',
            'option_a': 'Communication',
            'option_b': 'Accuracy and calculation',
            'option_c': 'Cleaning',
            'option_d': 'Design sense',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should a cashier do if a customer is angry? (lxe3f054)',
            'option_a': 'Respond angrily',
            'option_b': 'Stay calm and try to resolve the issue',
            'option_c': 'Ignore the customer',
            'option_d': 'Leave the counter',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should a cashier do if an item’s barcode doesn’t scan? (gxo61k46)',
            'option_a': 'Return the item',
            'option_b': 'Enter the code manually or call a supervisor',
            'option_c': 'Ask the customer to leave',
            'option_d': 'Give the item without billing',
            'correct_option': 'B'
        },
        {
            'question_text': 'What does “Float Money” mean? (lwf7nj7f)',
            'option_a': 'Initial cash provided at the start of the day',
            'option_b': 'Cash collected at the end of the day',
            'option_c': 'Total sales',
            'option_d': 'Refunds',
            'correct_option': 'A'
        },
        {
            'question_text': 'What should you do if there is a cash shortage or surplus? (wxy1lgnx)',
            'option_a': 'Hide it',
            'option_b': 'Report it immediately',
            'option_c': 'Blame someone else',
            'option_d': 'Report it the next day',
            'correct_option': 'B'
        },
        {
            'question_text': 'What does “Refund” mean in POS terms? (mxg27188)',
            'option_a': 'Create a new bill',
            'option_b': 'Return money to the customer',
            'option_c': 'Close the transaction',
            'option_d': 'Print another receipt',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should a cashier do if there is a power failure? (px90i377)',
            'option_a': 'Stop working',
            'option_b': 'Follow safety procedures, turn off systems, and inform customers',
            'option_c': 'Panic',
            'option_d': 'Continue working without light',
            'correct_option': 'B'
        },
        {
            'question_text': 'When processing a credit card, what should a cashier check? (vxxy1f9v)',
            'option_a': 'Card color',
            'option_b': 'Name and signature on the card',
            'option_c': 'Card design',
            'option_d': 'Machine sound',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the most important trait for a cashier? (xw0qsq8s)',
            'option_a': 'Honesty',
            'option_b': 'Fashion sense',
            'option_c': 'Fast talking',
            'option_d': 'Long nails',
            'correct_option': 'A'
        },
        {
            'question_text': 'Why is an “End of Day Report” prepared? (lxhvj9i6)',
            'option_a': 'Refuse',
            'option_b': 'Give a manual receipt',
            'option_c': 'Ask them to come the next day',
            'option_d': 'Hit the printer',
            'correct_option': 'B'
        },
        {
            'question_text': 'When should a cashier apply a discount? (qxr1gf18)',
            'option_a': 'Refuse',
            'option_b': 'Accept split payment if system allows',
            'option_c': 'Only accept cash',
            'option_d': 'Only accept card',
            'correct_option': 'B'
        },
        {
            'question_text': 'When should the cashier open the cash drawer? (zy394ym8)',
            'option_a': 'When no customer is nearby',
            'option_b': 'At all times',
            'option_c': 'Only during a transaction',
            'option_d': 'Whenever they want',
            'correct_option': 'C'
        },
        {
            'question_text': 'What should a cashier do if a customer bill is incorrect? (vxo8pvk6)',
            'option_a': 'Refuse to fix it',
            'option_b': 'Correct the bill and apologize',
            'option_c': 'Hide it from the manager',
            'option_d': 'Send the customer away',
            'correct_option': 'B'
        },
    ],

    'Site Civil Engineer': [
        {
            'question_text': 'What is the minimum cover required for reinforcement in a footing? (zz1ke4q8)',
            'option_a': '25 mm',
            'option_b': '40 mm',
            'option_c': '50 mm',
            'option_d': '75 mm',
            'correct_option': 'D'
        },
        {
            'question_text': 'What is the standard slump range for normal reinforced concrete used in foundations? (gx24u1r5)',
            'option_a': '25–50 mm',
            'option_b': '50–100 mm',
            'option_c': '75–150 mm',
            'option_d': '100–175 mm',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the typical water-cement ratio for M25 concrete? (nx7h0s73)',
            'option_a': '0.40',
            'option_b': '0.45',
            'option_c': '0.50',
            'option_d': '0.55',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the purpose of curing concrete? (ry7yo04o)',
            'option_a': 'To remove air voids',
            'option_b': 'To prevent shrinkage',
            'option_c': 'To maintain moisture for hydration',
            'option_d': 'To make surface smooth',
            'correct_option': 'C'
        },
        {
            'question_text': 'What does the cube test measure? (xyh3px04)',
            'option_a': '40 kg',
            'option_b': '45 kg',
            'option_c': '50 kg',
            'option_d': '55 kg',
            'correct_option': 'C'
        },
        {
            'question_text': 'What is the full form of NDT used in civil testing? (gxp2j841)',
            'option_a': 'Non-Durable Test',
            'option_b': 'Non-Destructive Test',
            'option_c': 'New Density Test',
            'option_d': 'Normal Dry Test',
            'correct_option': 'B'
        },
        {
            'question_text': 'Which test determines the bearing capacity of soil? (fy13tf66)',
            'option_a': '3 days',
            'option_b': '7 days',
            'option_c': '14 days',
            'option_d': '28 days',
            'correct_option': 'C'
        },
        {
            'question_text': 'What is the unit weight of reinforced concrete approximately? (xyypy996)',
            'option_a': '18 kN/m³',
            'option_b': '22 kN/m³',
            'option_c': '24 kN/m³',
            'option_d': '26 kN/m³',
            'correct_option': 'C'
        },
        {
            'question_text': 'What does “plinth level” represent? (jyexhhn4)',
            'option_a': 'Bar diameter',
            'option_b': 'Concrete grade',
            'option_c': 'Both A and B',
            'option_d': 'None of these',
            'correct_option': 'C'
        },
        {
            'question_text': 'Which IS code is used for plain and reinforced concrete? (sxp44u17)',
            'option_a': 'IS 383',
            'option_b': 'IS 456',
            'option_c': 'IS 10262',
            'option_d': 'IS 1893',
            'correct_option': 'B'
        },
        {
            'question_text': 'What does “camber” mean in road construction? (gw1z1r52)',
            'option_a': 'Rise at the center of the road for drainage',
            'option_b': 'Slope at the edge of the road',
            'option_c': 'Crack prevention',
            'option_d': 'Sub-base thickness',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the maximum height of concrete lift allowed at a time as per good practice? (ew2t46p5)',
            'option_a': 'Support fresh concrete until it gains strength',
            'option_b': 'Give color to concrete',
            'option_c': 'Reduce curing time',
            'option_d': 'None of these',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the minimum thickness of a damp proof course (DPC)? (gx5r2zl3)',
            'option_a': '10 mm',
            'option_b': '15 mm',
            'option_c': '20 mm',
            'option_d': '25 mm',
            'correct_option': 'B'
        },
        {
            'question_text': 'Which test measures the workability of concrete? (eyhj8p5h)',
            'option_a': 'Compaction Test',
            'option_b': 'Cube Test',
            'option_c': 'Slump Test',
            'option_d': 'Plate Load Test',
            'correct_option': 'C'
        },
        {
            'question_text': 'What is the typical permissible limit for steel reinforcement overlap in columns? (nx71093e)',
            'option_a': '24d',
            'option_b': '40d',
            'option_c': '50d',
            'option_d': '60d',
            'correct_option': 'B'
        },
        {
            'question_text': 'In pile foundations, what does “RCC” stand for? (swzj9t4m)',
            'option_a': 'Reinforced Cement Concrete',
            'option_b': 'Ready Concrete Column',
            'option_c': 'Rough Cement Construction',
            'option_d': 'Recast Concrete',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the purpose of providing expansion joints in concrete structures? (oym861hy)',
            'option_a': 'To add strength',
            'option_b': 'To reduce weight',
            'option_c': 'To allow for temperature movement',
            'option_d': 'To reduce load',
            'correct_option': 'C'
        },
        {
            'question_text': 'What is the minimum slope required for roof drainage? (twi329j3)',
            'option_a': 'To hold back soil or water pressure',
            'option_b': 'To divide rooms',
            'option_c': 'To support roof load',
            'option_d': 'To provide ventilation',
            'correct_option': 'A'
        },
    ],

    'Duct Man': [
        {
            'question_text': 'What is the primary purpose of HVAC ducts? (wx2jz24e)',
            'option_a': 'Save electricity',
            'option_b': 'Air distribution and ventilation',
            'option_c': 'Remove water',
            'option_d': 'Produce heat',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the function of a supply duct? (lxfh0f1z)',
            'option_a': 'Exhaust air outside',
            'option_b': 'Deliver cooled or heated air to rooms',
            'option_c': 'Remove water',
            'option_d': 'Filter dust',
            'correct_option': 'B'
        },
        {
            'question_text': 'What does a return duct do? (owrfnpsz)',
            'option_a': 'Sends air back to the AC unit',
            'option_b': 'Removes air outside',
            'option_c': 'Removes water',
            'option_d': 'Operates the fan',
            'correct_option': 'A'
        },
        {
            'question_text': 'Why is duct insulation important? (gw80115p)',
            'option_a': 'To maintain temperature and save energy',
            'option_b': 'To clean dust',
            'option_c': 'To remove water',
            'option_d': 'To increase fan speed',
            'correct_option': 'A'
        },
        {
            'question_text': 'Where are flexible ducts typically used? (uww9jsfj)',
            'option_a': 'In tight spaces within ceilings or walls',
            'option_b': 'Outdoor units',
            'option_c': 'Water drainage',
            'option_d': 'Compressors',
            'correct_option': 'A'
        },
        {
            'question_text': 'Why is seam sealing important in metal ducts? (iwzy457l)',
            'option_a': 'To prevent air leakage',
            'option_b': 'To clean dust',
            'option_c': 'To remove water',
            'option_d': 'To operate the fan',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the most important factor in duct sizing? (uxs9s260)',
            'option_a': 'Color',
            'option_b': 'Airflow volume (CFM)',
            'option_c': 'Material',
            'option_d': 'Weight',
            'correct_option': 'B'
        },
        {
            'question_text': 'Why are fire and safety regulations critical in duct installation? (yx7it0w0)',
            'option_a': 'Legal compliance only',
            'option_b': 'To prevent fire hazards and accidents',
            'option_c': 'To save time',
            'option_d': 'To save electricity',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the purpose of turning vanes in ducts? (sw76lx8p)',
            'option_a': 'To direct airflow',
            'option_b': 'To remove water',
            'option_c': 'To filter dust',
            'option_d': 'To save energy',
            'correct_option': 'A'
        },
        {
            'question_text': 'How are duct leaks typically tested? (rx7wzo4z)',
            'option_a': 'Visual inspection',
            'option_b': 'Smoke test or pressure test',
            'option_c': 'Color test',
            'option_d': 'Temperature test',
            'correct_option': 'B'
        },
        {
            'question_text': 'Why is static pressure in ducts important? (iweo67ur)',
            'option_a': 'To ensure efficient airflow',
            'option_b': 'To save electricity',
            'option_c': 'To remove water',
            'option_d': 'To filter dust',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the difference between a supply air register and a grille? (yw97lr46)',
            'option_a': 'Registers have a damper; grilles do not',
            'option_b': 'Grilles are stronger',
            'option_c': 'Both are the same',
            'option_d': 'Registers are installed outdoors',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is important when selecting duct material? (xx9hmlwq)',
            'option_a': 'Color',
            'option_b': 'Strength, durability, and corrosion resistance',
            'option_c': 'Price',
            'option_d': 'Weight',
            'correct_option': 'B'
        },
        {
            'question_text': 'When should ducts be cleaned? (txg81u8s)',
            'option_a': 'Daily',
            'option_b': 'To maintain HVAC efficiency and air quality',
            'option_c': 'Never',
            'option_d': 'Only outdoor units',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the most common method for duct connections? (yx6195tm)',
            'option_a': 'Welding',
            'option_b': 'Sheet metal screws and mastic sealant',
            'option_c': 'Glue',
            'option_d': 'Tape',
            'correct_option': 'B'
        },
        {
            'question_text': 'How should supply and return ducts be positioned in a layout? (fx3uwwz7)',
            'option_a': 'Together',
            'option_b': 'At proper distances for balanced and unobstructed airflow',
            'option_c': 'Close together',
            'option_d': 'Randomly',
            'correct_option': 'B'
        },
        {
            'question_text': 'What are common causes of duct noise? (sznvo1y5)',
            'option_a': 'Incorrect sizing',
            'option_b': 'Damper problems',
            'option_c': 'Vibration',
            'option_d': 'All of the above',
            'correct_option': 'D'
        },
        {
            'question_text': 'What should be done if a duct joint leaks? (mxjz1vin)',
            'option_a': 'Ignore it',
            'option_b': 'Seal with mastic or sealant',
            'option_c': 'Apply tape',
            'option_d': 'Replace the duct',
            'correct_option': 'B'
        },
        {
            'question_text': 'Why are duct hangers and supports necessary? (kw27m6t2)',
            'option_a': 'To bear weight and reduce vibration',
            'option_b': 'For aesthetics',
            'option_c': 'To remove water',
            'option_d': 'To save energy',
            'correct_option': 'A'
        },
        {
            'question_text': 'Why are smoke detectors and fire dampers installed in ducts? (wx61hj9j)',
            'option_a': 'Legal compliance only',
            'option_b': 'Fire and safety protection',
            'option_c': 'To improve efficiency',
            'option_d': 'To save electricity',
            'correct_option': 'B'
        },
        {
            'question_text': 'How can duct pressure drop be minimized? (hz51euj4)',
            'option_a': 'Use larger duct sizes',
            'option_b': 'Reduce bends',
            'option_c': 'Smooth internal surfaces',
            'option_d': 'All of the above',
            'correct_option': 'D'
        },
        {
            'question_text': 'Why is excessive bending of flexible ducts harmful? (jz9w8zx8)',
            'option_a': 'Restricts airflow',
            'option_b': 'Increases noise',
            'option_c': 'Causes energy loss',
            'option_d': 'All of the above',
            'correct_option': 'D'
        },
        {
            'question_text': 'What does the R-value of duct insulation indicate? (fx154m39)',
            'option_a': 'Material strength',
            'option_b': 'Thermal resistance',
            'option_c': 'Weight',
            'option_d': 'Color',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is checked during a post-installation duct system test? (izl0pn3k)',
            'option_a': 'Airflow (CFM)',
            'option_b': 'Static pressure',
            'option_c': 'Leak test',
            'option_d': 'All of the above',
            'correct_option': 'D'
        },
        {
            'question_text': 'What are the benefits of proper duct design? (gz9y487n)',
            'option_a': 'Efficient airflow',
            'option_b': 'Energy savings',
            'option_c': 'Noise reduction',
            'option_d': 'All of the above',
            'correct_option': 'D'
        },
    ],

    'Load & Unload Worker': [
        {
            'question_text': 'What is the main purpose of loading and unloading work? (sw6004t8)',
            'option_a': 'To safely move goods from one place to another',
            'option_b': 'To count goods',
            'option_c': 'To sell goods',
            'option_d': 'To clean goods',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the most important safety rule when lifting heavy items? (oxio8q2e)',
            'option_a': 'Bend from the waist',
            'option_b': 'Bend your knees while lifting',
            'option_c': 'Lift quickly',
            'option_d': 'Lift with a jerk',
            'correct_option': 'B'
        },
        {
            'question_text': 'Which equipment helps in lifting heavy loads? (jww12i5y)',
            'option_a': 'Forklift',
            'option_b': 'Screwdriver',
            'option_c': 'Hammer',
            'option_d': 'Drill',
            'correct_option': 'A'
        },
        {
            'question_text': 'What should be maintained while unloading goods? (tx5m6f1o)',
            'option_a': 'Speed',
            'option_b': 'Balance',
            'option_c': 'Time',
            'option_d': 'Temperature',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should you do if a package is damaged? (ix9eyqu1)',
            'option_a': 'Ignore it',
            'option_b': 'Inform the supervisor',
            'option_c': 'Throw it away',
            'option_d': 'Repair it yourself',
            'correct_option': 'B'
        },
        {
            'question_text': 'What can happen if you lift more than the allowed weight limit? (fz24g3i4)',
            'option_a': 'Physical injury',
            'option_b': 'Goods may break',
            'option_c': 'Accidents may occur',
            'option_d': 'All of the above',
            'correct_option': 'D'
        },
        {
            'question_text': 'Why should workers wear gloves while lifting? (lx36s169)',
            'option_a': 'To keep hands warm',
            'option_b': 'To protect hands from cuts and injuries',
            'option_c': 'For style',
            'option_d': 'To reduce grip',
            'correct_option': 'B'
        },
        {
            'question_text': 'Which tool is used to move goods from a truck or container? (kxi58m7m)',
            'option_a': 'Wrench',
            'option_b': 'Pallet jack',
            'option_c': 'Spanner',
            'option_d': 'Saw',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should you check before lifting a load? (swn69fyo)',
            'option_a': 'Weight of the load and if the path is clear',
            'option_b': 'The time of day',
            'option_c': 'How many people are watching',
            'option_d': 'How long it will take',
            'correct_option': 'A'
        },
        {
            'question_text': 'What should you do if the load is too heavy? (vxr7n34k)',
            'option_a': 'Lift it alone',
            'option_b': 'Ask for help',
            'option_c': 'Leave it',
            'option_d': 'Hide it',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the most important safety rule in a loading area? (ewr8u44g)',
            'option_a': 'Wear proper shoes and uniform',
            'option_b': 'Eat and drink while working',
            'option_c': 'Work quickly',
            'option_d': 'Talk loudly',
            'correct_option': 'A'
        },
        {
            'question_text': 'Why are pallets used? (xwno04ev)',
            'option_a': 'To make lifting and moving goods easier',
            'option_b': 'To reduce weight',
            'option_c': 'To hide goods',
            'option_d': 'To save space',
            'correct_option': 'A'
        },
        {
            'question_text': 'Which body part should remain straight while lifting? (nx947z36)',
            'option_a': 'Arms',
            'option_b': 'Back',
            'option_c': 'Knees',
            'option_d': 'Shoulders',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should you ensure before unloading goods? (vww23w5y)',
            'option_a': 'The area below is clean and safe',
            'option_b': 'Unload quickly',
            'option_c': 'Throw the goods',
            'option_d': 'Open all boxes',
            'correct_option': 'A'
        },
        {
            'question_text': 'How can slips and falls be prevented in a loading area? (ow17t4gk)',
            'option_a': 'By keeping the floor clean and dry',
            'option_b': 'By keeping it wet',
            'option_c': 'By using a soft carpet',
            'option_d': 'By working on a slope',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the correct way to breathe while lifting? (qxu1mxr5)',
            'option_a': 'Hold your breath',
            'option_b': 'Breathe slowly and steadily',
            'option_c': 'Keep your mouth closed',
            'option_d': 'Breathe fast',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should you do when working near a forklift? (vw960t54)',
            'option_a': 'Stay at a safe distance',
            'option_b': 'Walk under the forks',
            'option_c': 'Shout to get attention',
            'option_d': 'Wave your hands',
            'correct_option': 'A'
        },
        {
            'question_text': 'How should loads be arranged for proper balance? (jw64vmf6)',
            'option_a': 'Heavy items at the bottom, light items on top',
            'option_b': 'Light items at the bottom',
            'option_c': 'Stack as high as possible',
            'option_d': 'On one side',
            'correct_option': 'A'
        },
        {
            'question_text': 'What should you do if you feel dizzy while lifting? (ow34u1v4)',
            'option_a': 'Drop the load and sit down immediately',
            'option_b': 'Keep working',
            'option_c': 'Run away',
            'option_d': 'Hide it from the supervisor',
            'correct_option': 'A'
        },
        {
            'question_text': 'Why is teamwork important during loading and unloading? (ewn134w3)',
            'option_a': 'Arranged properly with balance and order',
            'option_b': 'Fill it as much as possible',
            'option_c': 'Stack it very high',
            'option_d': 'Randomly',
            'correct_option': 'A'
        },
        {
            'question_text': 'How can back pain be prevented during lifting work? (gwk0148h)',
            'option_a': 'Use proper lifting techniques',
            'option_b': 'Lift heavier loads',
            'option_c': 'Bend quickly',
            'option_d': 'Sit for long periods',
            'correct_option': 'A'
        },
        {
            'question_text': 'Why are warning signs important in a loading area? (twvv45f9)',
            'option_a': 'To prevent accidents',
            'option_b': 'For decoration',
            'option_c': 'To show colors',
            'option_d': 'For appearance only',
            'correct_option': 'A'
        },
        {
            'question_text': 'What should be done if goods move or shift in a vehicle? (hwo48v4e)',
            'option_a': 'Safety and caution',
            'option_b': 'Speed',
            'option_c': 'Noise',
            'option_d': 'Less time',
            'correct_option': 'A'
        },
    ],

    'Plumber': [
        {
            'question_text': 'What is the standard pipe size used for domestic water supply to a wash basin? (zyf788p7)',
            'option_a': '1 inch',
            'option_b': '¾ inch',
            'option_c': '½ inch',
            'option_d': '1¼ inch',
            'correct_option': 'C'
        },
        {
            'question_text': 'Which tool is used to cut PVC pipes? (xy9wvvkl)',
            'option_a': 'Pipe wrench',
            'option_b': 'Pipe cutter',
            'option_c': 'Hacksaw',
            'option_d': 'Reamer',
            'correct_option': 'C'
        },
        {
            'question_text': 'What is the main purpose of a trap in a plumbing system? (vx22818f)',
            'option_a': '0.5 bar',
            'option_b': '2 to 3 bar',
            'option_c': '5 bar',
            'option_d': '10 bar',
            'correct_option': 'B'
        },
        {
            'question_text': 'Which type of pipe is most suitable for hot water supply? (zy4qj9n3)',
            'option_a': 'PVC',
            'option_b': 'GI (Galvanized Iron)',
            'option_c': 'CPVC',
            'option_d': 'UPVC',
            'correct_option': 'C'
        },
        {
            'question_text': 'What is the minimum slope required for a horizontal drainage pipe? (kw235lz6)',
            'option_a': 'Control flow',
            'option_b': 'Prevent backflow',
            'option_c': 'Filter impurities',
            'option_d': 'Reduce pressure',
            'correct_option': 'A'
        },
        {
            'question_text': 'Which fitting is used to join two pipes at a 90° angle? (ow21u5n0)',
            'option_a': 'Elbow',
            'option_b': 'Tee',
            'option_c': 'Coupling',
            'option_d': 'Union',
            'correct_option': 'A'
        },
        {
            'question_text': 'Which test is done to check water leakage in newly installed pipes? (ex45y7es)',
            'option_a': 'Air test',
            'option_b': 'Pressure test',
            'option_c': 'Smoke test',
            'option_d': 'Flow test',
            'correct_option': 'B'
        },
        {
            'question_text': 'Which type of joint is used for connecting copper pipes? (kx622hp9)',
            'option_a': 'Threaded joint',
            'option_b': 'Compression joint',
            'option_c': 'Solvent joint',
            'option_d': 'Welded joint',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the full form of PVC? (nw286w7t)',
            'option_a': 'Poly Vinyl Chloride',
            'option_b': 'Poly Vinyl Compound',
            'option_c': 'Plastic Vinyl Chloride',
            'option_d': 'Poly Viscose Compound',
            'correct_option': 'A'
        },
        {
            'question_text': 'Which device prevents water from flowing backward? (zxh334rh)',
            'option_a': 'Stop valve',
            'option_b': 'Check valve',
            'option_c': 'Gate valve',
            'option_d': 'Float valve',
            'correct_option': 'B'
        },
        {
            'question_text': 'Which tool is used to remove burrs from cut pipes? (iw316711)',
            'option_a': 'Reamer',
            'option_b': 'Threader',
            'option_c': 'Wrench',
            'option_d': 'Plier',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the main cause of water hammer in pipelines? (owukv546)',
            'option_a': 'Vent pipe',
            'option_b': 'Valve',
            'option_c': 'Vertical pipe',
            'option_d': 'Vacuum line',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the color code for hot water pipe in Gulf countries? (qxsiq01o)',
            'option_a': 'Blue',
            'option_b': 'Red',
            'option_c': 'Green',
            'option_d': 'Yellow',
            'correct_option': 'B'
        },
        {
            'question_text': 'Which of the following is used for joining GI pipes? (iwh8lfh7)',
            'option_a': 'Threaded joint',
            'option_b': 'Solvent joint',
            'option_c': 'Welded joint',
            'option_d': 'Flanged joint',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the function of a float valve in a water tank? (gw4tl722)',
            'option_a': 'Maintain water level automatically',
            'option_b': 'Drain the tank',
            'option_c': 'Increase pressure',
            'option_d': 'Stop backflow',
            'correct_option': 'A'
        },
        {
            'question_text': 'Which fitting connects two different sizes of pipes? (xwyx0r22)',
            'option_a': 'Reducer',
            'option_b': 'Elbow',
            'option_c': 'Tee',
            'option_d': 'Socket',
            'correct_option': 'A'
        },
        {
            'question_text': 'Which type of wrench is commonly used by plumbers? (exnz395i)',
            'option_a': 'Carry waste water',
            'option_b': 'Balance air pressure in drainage system',
            'option_c': 'Supply air to fixtures',
            'option_d': 'Prevent overflow',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the standard thread type used in plumbing pipes? (jwojp7px)',
            'option_a': 'BSP (British Standard Pipe)',
            'option_b': 'NPT (National Pipe Thread)',
            'option_c': 'Metric',
            'option_d': 'JIS',
            'correct_option': 'A'
        },
        {
            'question_text': 'Which of the following materials is NOT used for drainage pipes? (uy528v5z)',
            'option_a': 'PVC',
            'option_b': 'CI (Cast Iron)',
            'option_c': 'CPVC',
            'option_d': 'Lead',
            'correct_option': 'C'
        },
        {
            'question_text': 'What is the purpose of a clean-out in plumbing? (zx5ntuzm)',
            'option_a': 'For pipe testing',
            'option_b': 'For cleaning blockages',
            'option_c': 'For pressure relief',
            'option_d': 'For venting gases',
            'correct_option': 'B'
        },
        {
            'question_text': 'Which of the following safety gear is most essential for a plumber? (pz43ytl4)',
            'option_a': 'Helmet',
            'option_b': 'Gloves',
            'option_c': 'Safety glasses',
            'option_d': 'All of the above',
            'correct_option': 'D'
        },
    ],

    'Kitchen Helper': [
        {
            'question_text': 'What is meant by “Cross Contamination” in the kitchen? (exp71x54)',
            'option_a': 'Overcooking food',
            'option_b': 'Mixing raw and cooked food',
            'option_c': 'Adding too much salt',
            'option_d': 'Washing dishes late',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should be the correct temperature for storing meat? (oxw28gvs)',
            'option_a': '15°C',
            'option_b': '0°C to 4°C',
            'option_c': '10°C',
            'option_d': '25°C',
            'correct_option': 'B'
        },
        {
            'question_text': 'Which knife is safest for cutting vegetables? (zxi4t8oj)',
            'option_a': 'Dull knife',
            'option_b': 'Sharp knife',
            'option_c': 'Rusty knife',
            'option_d': 'Bent knife',
            'correct_option': 'B'
        },
        {
            'question_text': 'When should you wash your hands in the kitchen? (ky21m138)',
            'option_a': 'Only after work',
            'option_b': 'Only after eating',
            'option_c': 'Before and after touching food',
            'option_d': 'Once a day',
            'correct_option': 'C'
        },
        {
            'question_text': 'What temperature should the dishwashing water be? (uy77jw37)',
            'option_a': 'Cold',
            'option_b': 'Lukewarm',
            'option_c': 'Very hot',
            'option_d': 'Ice cold',
            'correct_option': 'C'
        },
        {
            'question_text': 'What does “Personal Hygiene” mean in the kitchen? (mxmy23p2)',
            'option_a': 'Changing clothes',
            'option_b': 'Cleanliness and personal care',
            'option_c': 'Tasting food',
            'option_d': 'Finishing work on time',
            'correct_option': 'B'
        },
        {
            'question_text': 'What does the “FIFO” rule mean? (rx8f0jgm)',
            'option_a': 'To improve taste',
            'option_b': 'Use old stock first',
            'option_c': 'To wash dishes',
            'option_d': 'To save electricity',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should you do if water spills on the kitchen floor? (my6702k8)',
            'option_a': 'Tell someone else',
            'option_b': 'Ignore it',
            'option_c': 'Clean it immediately',
            'option_d': 'Leave it for later',
            'correct_option': 'C'
        },
        {
            'question_text': 'When using a microwave, what should you always do? (vx5yv9je)',
            'option_a': 'Use metal dishes',
            'option_b': 'Cover the food',
            'option_c': 'Burn plastic',
            'option_d': 'Leave it unattended',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the ideal freezer temperature? (uyj9ijz5)',
            'option_a': '5°C',
            'option_b': '0°C',
            'option_c': '-18°C',
            'option_d': '10°C',
            'correct_option': 'C'
        },
        {
            'question_text': 'What should you do first if a fire starts in the kitchen? (qy4s90kn)',
            'option_a': 'Run away',
            'option_b': 'Throw water',
            'option_c': 'Turn off the gas',
            'option_d': 'Do nothing',
            'correct_option': 'C'
        },
        {
            'question_text': 'Why should gloves be worn in the kitchen? (ry0386ej)',
            'option_a': 'To keep hands warm',
            'option_b': 'To avoid dirty hands',
            'option_c': 'To prevent germs from spreading',
            'option_d': 'For fashion',
            'correct_option': 'C'
        },
        {
            'question_text': 'What must you do before starting work in the kitchen? (ex1n1961)',
            'option_a': 'Play music',
            'option_b': 'Wash your hands',
            'option_c': 'Taste food',
            'option_d': 'Call a friend',
            'correct_option': 'B'
        },
        {
            'question_text': 'Which soap is suitable for washing dishes? (hy9rj4u4)',
            'option_a': 'Laundry soap',
            'option_b': 'Body wash',
            'option_c': 'Dishwashing liquid',
            'option_d': 'Shampoo',
            'correct_option': 'C'
        },
        {
            'question_text': 'What should you do if you find hair in food? (ly6z9p92)',
            'option_a': 'Remove it and eat',
            'option_b': 'Hide it',
            'option_c': 'Discard the food',
            'option_d': 'Reheat the food',
            'correct_option': 'C'
        },
        {
            'question_text': 'What does “Defrosting” mean? (kx1v3los)',
            'option_a': 'Freezing food',
            'option_b': 'Melting frozen food',
            'option_c': 'Cooking food',
            'option_d': 'Decorating food',
            'correct_option': 'B'
        },
        {
            'question_text': 'How can kitchen noise be minimized? (ox6mp6ro)',
            'option_a': 'Talk loudly',
            'option_b': 'Handle tools carefully',
            'option_c': 'Throw things',
            'option_d': 'Drop utensils',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should you do if someone is injured in the kitchen? (xx395xnk)',
            'option_a': 'Ignore it',
            'option_b': 'Give first aid immediately',
            'option_c': 'Make jokes',
            'option_d': 'Do nothing',
            'correct_option': 'B'
        },
        {
            'question_text': 'How can food wastage be prevented? (yxzm291g)',
            'option_a': 'Cook extra food',
            'option_b': 'Store and plan properly',
            'option_c': 'Throw leftovers',
            'option_d': 'Ignore leftovers',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should every kitchen worker wear during work? (gx5z0018)',
            'option_a': 'Shoes',
            'option_b': 'Apron',
            'option_c': 'Watch',
            'option_d': 'Sunglasses',
            'correct_option': 'B'
        },
        {
            'question_text': 'Why should food containers be labeled? (kxvrk6x2)',
            'option_a': 'To change color',
            'option_b': 'To identify contents and dates',
            'option_c': 'To look attractive',
            'option_d': 'No reason',
            'correct_option': 'B'
        },
        {
            'question_text': 'What type of kitchen floor is best? (wx6m63r2)',
            'option_a': 'Slippery',
            'option_b': 'Clean and dry',
            'option_c': 'Dirty',
            'option_d': 'Greasy',
            'correct_option': 'B'
        },
        {
            'question_text': 'What does “Sanitization” mean? (xx98pppu)',
            'option_a': 'Beautifying surfaces',
            'option_b': 'Killing germs',
            'option_c': 'Heating water',
            'option_d': 'Improving taste',
            'correct_option': 'B'
        },
        {
            'question_text': 'How soon should leftover food be refrigerated after cooking? (vww8p24m)',
            'option_a': 'Within 1 hour',
            'option_b': 'After 5 hours',
            'option_c': 'Next day',
            'option_d': 'After 10 hours',
            'correct_option': 'A'
        },
        {
            'question_text': 'Why is a cleaning schedule important in the kitchen? (xx2kgx56)',
            'option_a': 'To waste time',
            'option_b': 'To maintain hygiene',
            'option_c': 'For decoration',
            'option_d': 'It’s not important',
            'correct_option': 'B'
        },
    ],

    'Electrician': [
        {
            'question_text': 'What is the standard frequency of electrical supply in Gulf countries? (pw6y4xti)',
            'option_a': '50 Hz',
            'option_b': '60 Hz',
            'option_c': '100 Hz',
            'option_d': '120 Hz',
            'correct_option': 'A'
        },
        {
            'question_text': 'Which color wire is used for the earth connection in a single-phase circuit? (nxj275x0)',
            'option_a': '110 V',
            'option_b': '230 V',
            'option_c': '415 V',
            'option_d': '12 V',
            'correct_option': 'B'
        },
        {
            'question_text': 'Which device is used to protect a circuit from overcurrent? (mwjm237e)',
            'option_a': 'MCB',
            'option_b': 'Contactor',
            'option_c': 'Timer',
            'option_d': 'Relay',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the full form of MCB? (jx8h8zi2)',
            'option_a': 'Main Circuit Board',
            'option_b': 'Miniature Circuit Breaker',
            'option_c': 'Main Current Breaker',
            'option_d': 'Multiple Circuit Block',
            'correct_option': 'B'
        },
        {
            'question_text': 'Which instrument is used to measure electric current? (ext3s577)',
            'option_a': 'Voltmeter',
            'option_b': 'Ammeter',
            'option_c': 'Ohmmeter',
            'option_d': 'Megger',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the main function of an ELCB or RCCB? (oyz2vvnt)',
            'option_a': '60°',
            'option_b': '90°',
            'option_c': '120°',
            'option_d': '180°',
            'correct_option': 'C'
        },
        {
            'question_text': 'Which wire carries the return current in an electrical circuit? (jxh8pgpy)',
            'option_a': 'Phase wire',
            'option_b': 'Neutral wire',
            'option_c': 'Earth wire',
            'option_d': 'Control wire',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the standard color for neutral wire in Gulf countries? (eyvj4tnt)',
            'option_a': 'Red',
            'option_b': 'Black',
            'option_c': 'Blue',
            'option_d': 'Yellow',
            'correct_option': 'C'
        },
        {
            'question_text': 'What is the function of a capacitor in an electric motor? (txusouhi)',
            'option_a': 'Increase resistance',
            'option_b': 'Improve power factor and help in starting torque',
            'option_c': 'Reduce voltage',
            'option_d': 'Protect winding',
            'correct_option': 'B'
        },
        {
            'question_text': 'Which instrument is used to check insulation resistance? (zx2nev9z)',
            'option_a': 'Ammeter',
            'option_b': 'Megger',
            'option_c': 'Voltmeter',
            'option_d': 'Ohmmeter',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the full form of PPE? (zx06uhim)',
            'option_a': 'Personal Power Equipment',
            'option_b': 'Personal Protective Equipment',
            'option_c': 'Portable Protection Equipment',
            'option_d': 'Proper Power Element',
            'correct_option': 'B'
        },
        {
            'question_text': 'Which device automatically disconnects power in case of a short circuit? (zyvs065p)',
            'option_a': 'Contactor',
            'option_b': 'Relay',
            'option_c': 'Circuit Breaker',
            'option_d': 'Fuse only',
            'correct_option': 'C'
        },
        {
            'question_text': 'What is the unit of electrical power? (iy3m78sr)',
            'option_a': 'Ampere',
            'option_b': 'Volt',
            'option_c': 'Watt',
            'option_d': 'Ohm',
            'correct_option': 'C'
        },
        {
            'question_text': 'Which type of connection is used in domestic power circuits? (zy5lfrwi)',
            'option_a': 'Star connection',
            'option_b': 'Delta connection',
            'option_c': 'Parallel connection',
            'option_d': 'Series connection',
            'correct_option': 'C'
        },
        {
            'question_text': 'What is the resistance of a good conductor? (kx35z9lh)',
            'option_a': 'High',
            'option_b': 'Low',
            'option_c': 'Medium',
            'option_d': 'Infinite',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the color code of live wire in Gulf countries? (mwn94q99)',
            'option_a': 'Red or Brown',
            'option_b': 'Blue',
            'option_c': 'Green',
            'option_d': 'Black',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the purpose of earthing in an electrical installation? (xxm991wx)',
            'option_a': 'To increase voltage',
            'option_b': 'To protect from electric shock',
            'option_c': 'To control current',
            'option_d': 'To reduce temperature',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the formula for electrical power? (pxjl15v9)',
            'option_a': 'P = V/I',
            'option_b': 'P = I × V',
            'option_c': 'P = V / R',
            'option_d': 'P = R × I²',
            'correct_option': 'B'
        },
        {
            'question_text': 'Which tool is used to strip the insulation from wires? (rx1olr57)',
            'option_a': 'Pliers',
            'option_b': 'Wire stripper',
            'option_c': 'Screwdriver',
            'option_d': 'Hacksaw',
            'correct_option': 'B'
        },
        {
            'question_text': 'Which of the following devices is used to control a lamp from two locations? (ox5812w8)',
            'option_a': 'One-way switch',
            'option_b': 'Two-way switch',
            'option_c': 'Push button switch',
            'option_d': 'Rotary switch',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the main function of a fuse? (gx13e56u)',
            'option_a': 'To connect the circuit',
            'option_b': 'To protect the circuit from overcurrent',
            'option_c': 'To increase voltage',
            'option_d': 'To control load',
            'correct_option': 'B'
        },
        {
            'question_text': 'What happens if the neutral wire is disconnected in a single-phase circuit? (xy52mxg1)',
            'option_a': 'Equipment works normally',
            'option_b': 'Overvoltage occurs',
            'option_c': 'Circuit will open and stop working',
            'option_d': 'Current increases',
            'correct_option': 'C'
        },
        {
            'question_text': 'Which type of motor is commonly used in ceiling fans? (ux63279n)',
            'option_a': 'DC shunt motor',
            'option_b': 'Single-phase induction motor',
            'option_c': 'Synchronous motor',
            'option_d': 'Stepper motor',
            'correct_option': 'B'
        },
    ],

    'HVAC Technician': [
        {
            'question_text': 'What does HVAC stand for? (nx7wzhi3)',
            'option_a': 'Heating, Ventilation and Air Cooling',
            'option_b': 'Heating, Ventilation and Air Conditioning',
            'option_c': 'Heat, Vacuum and Air Circulation',
            'option_d': 'High Voltage Air Control',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the normal pressure of an R-410A refrigerant in running condition? (ywesf05q)',
            'option_a': 'Low side 120 psi / High side 400 psi',
            'option_b': 'Low side 40 psi / High side 150 psi',
            'option_c': 'Low side 80 psi / High side 250 psi',
            'option_d': 'Low side 250 psi / High side 600 psi',
            'correct_option': 'A'
        },
        {
            'question_text': 'Which refrigerant is commonly used in split air conditioners today? (sx7e9p83)',
            'option_a': 'R-22',
            'option_b': 'R-410A',
            'option_c': 'R-134A',
            'option_d': 'Ammonia',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the main function of the compressor in an HVAC system? (hw1505h8)',
            'option_a': 'Condenser',
            'option_b': 'Evaporator',
            'option_c': 'Compressor',
            'option_d': 'Filter drier',
            'correct_option': 'A'
        },
        {
            'question_text': 'Which component absorbs heat from the indoor air? (qxe0v6s8)',
            'option_a': 'Condenser',
            'option_b': 'Evaporator coil',
            'option_c': 'Expansion valve',
            'option_d': 'Compressor',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the purpose of the expansion valve? (jx46f139)',
            'option_a': 'Increase pressure',
            'option_b': 'Reduce refrigerant pressure and temperature',
            'option_c': 'Store refrigerant',
            'option_d': 'Remove moisture',
            'correct_option': 'B'
        },
        {
            'question_text': 'Which instrument is used to measure refrigerant pressure? (ox42pwkh)',
            'option_a': 'Clamp meter',
            'option_b': 'Manifold gauge',
            'option_c': 'Vacuum pump',
            'option_d': 'Thermometer',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should be the vacuum pressure before charging refrigerant in a system? (zxx64xzx)',
            'option_a': '1000 microns',
            'option_b': '500 microns or below',
            'option_c': '1500 microns',
            'option_d': '2000 microns',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the unit of refrigeration capacity? (rx8qt21i)',
            'option_a': 'Volt',
            'option_b': 'Ton',
            'option_c': 'Pascal',
            'option_d': 'Ohm',
            'correct_option': 'B'
        },
        {
            'question_text': '1 Ton of refrigeration is equal to how many BTU per hour? (lx5xn1i1)',
            'option_a': '10,000 BTU/hr',
            'option_b': '12,000 BTU/hr',
            'option_c': '24,000 BTU/hr',
            'option_d': '5,000 BTU/hr',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the normal superheat temperature range for a properly charged system? (qyqt0mnm)',
            'option_a': '2–4°C',
            'option_b': '5–8°C',
            'option_c': '8–12°C',
            'option_d': '15–20°C',
            'correct_option': 'C'
        },
        {
            'question_text': 'What type of compressor is most common in split AC units? (wx6r4js9)',
            'option_a': 'Reciprocating',
            'option_b': 'Rotary',
            'option_c': 'Screw',
            'option_d': 'Centrifugal',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the function of a filter drier? (lx5n37sv)',
            'option_a': 'Filter dust only',
            'option_b': 'Remove moisture and impurities from refrigerant',
            'option_c': 'Store refrigerant',
            'option_d': 'Increase cooling',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the recommended air filter cleaning interval in HVAC systems? (pyi8j457)',
            'option_a': 'Daily',
            'option_b': 'Weekly',
            'option_c': 'Monthly',
            'option_d': 'Yearly',
            'correct_option': 'C'
        },
        {
            'question_text': 'Which tool is used to check the amperage of a compressor motor? (xxv3mq4r)',
            'option_a': 'Multimeter',
            'option_b': 'Clamp meter',
            'option_c': 'Pressure gauge',
            'option_d': 'Thermostat',
            'correct_option': 'B'
        },
        {
            'question_text': 'What happens if the air filter is clogged? (vyg6nm30)',
            'option_a': 'Airflow increases',
            'option_b': 'System efficiency improves',
            'option_c': 'Airflow decreases and evaporator coil may freeze',
            'option_d': 'Compressor runs smoothly',
            'correct_option': 'C'
        },
        {
            'question_text': 'Which gas is considered environmentally friendly (ozone safe)? (wxfoeu29)',
            'option_a': 'R-22',
            'option_b': 'R-134A',
            'option_c': 'R-12',
            'option_d': 'R-502',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the main purpose of a thermostat? (zwzpo93p)',
            'option_a': 'To control temperature automatically',
            'option_b': 'To measure humidity',
            'option_c': 'To increase fan speed',
            'option_d': 'To detect gas leak',
            'correct_option': 'A'
        },
        {
            'question_text': 'What should be checked first when an AC unit is not cooling? (ux4h2718)',
            'option_a': 'Refrigerant charge',
            'option_b': 'Thermostat setting and power supply',
            'option_c': 'Condenser coil size',
            'option_d': 'Duct insulation',
            'correct_option': 'B'
        },
        {
            'question_text': 'What type of current is used in most HVAC systems? (yw90kk89)',
            'option_a': 'AC (Alternating Current)',
            'option_b': 'DC (Direct Current)',
            'option_c': 'Pulsed current',
            'option_d': 'Static current',
            'correct_option': 'A'
        },
        {
            'question_text': 'Which safety device protects the compressor from overload? (zxn2sl75)',
            'option_a': 'Thermostat',
            'option_b': 'Overload protector',
            'option_c': 'Contactor',
            'option_d': 'Relay',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the purpose of insulation on suction lines? (nx6ilxi9)',
            'option_a': 'Prevent refrigerant leaks',
            'option_b': 'Reduce heat gain and prevent condensation',
            'option_c': 'Increase pressure',
            'option_d': 'Improve oil flow',
            'correct_option': 'B'
        },
        {
            'question_text': 'Which tool is used to remove air and moisture from the system before charging? (wx8ee032)',
            'option_a': 'Manifold gauge',
            'option_b': 'Vacuum pump',
            'option_c': 'Leak detector',
            'option_d': 'Thermometer',
            'correct_option': 'B'
        },
        {
            'question_text': 'What happens if refrigerant is overcharged in a system? (ixmy044z)',
            'option_a': 'Cooling improves',
            'option_b': 'Compressor may overheat and system efficiency drops',
            'option_c': 'Power consumption decreases',
            'option_d': 'Pressure becomes low',
            'correct_option': 'B'
        },
    ],

    'Accountant': [
        {
            'question_text': 'What is the primary role of an accountant? (xx0z9r6y)',
            'option_a': 'Preparing budgets',
            'option_b': 'Recording and analyzing financial transactions',
            'option_c': 'Marketing products',
            'option_d': 'Overseeing production',
            'correct_option': 'B'
        },
        {
            'question_text': 'What do assets represent? (lx6sut53)',
            'option_a': 'Company liabilities',
            'option_b': 'Company ownership and resources',
            'option_c': 'Profit',
            'option_d': 'Loss',
            'correct_option': 'B'
        },
        {
            'question_text': 'What does liability mean? (qwp60rmp)',
            'option_a': 'Company obligations and debts',
            'option_b': 'Company profit',
            'option_c': 'Company assets',
            'option_d': 'Tax',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is equity? (uwig0y80)',
            'option_a': 'Shareholders’ ownership in the company',
            'option_b': 'Company debt',
            'option_c': 'Company profit',
            'option_d': 'Company revenue',
            'correct_option': 'A'
        },
        {
            'question_text': 'What does a balance sheet show? (tx6j96fz)',
            'option_a': 'Income and expenses',
            'option_b': 'Company’s assets, liabilities, and shareholders’ equity',
            'option_c': 'Cash details',
            'option_d': 'Tax information',
            'correct_option': 'B'
        },
        {
            'question_text': 'What information does an income statement provide? (oxo6t4s9)',
            'option_a': 'Company value',
            'option_b': 'Revenue, expenses, and profit/loss',
            'option_c': 'Company assets',
            'option_d': 'Company debts',
            'correct_option': 'B'
        },
        {
            'question_text': 'How many effects does each transaction have in double-entry accounting? (gx5f77tv)',
            'option_a': 'One',
            'option_b': 'Two',
            'option_c': 'Three',
            'option_d': 'Four',
            'correct_option': 'B'
        },
        {
            'question_text': 'In which account are debits and credits recorded? (ux50r2hr)',
            'option_a': 'Cash Flow',
            'option_b': 'General Ledger',
            'option_c': 'Trial Balance',
            'option_d': 'Income Statement',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the purpose of a trial balance? (hx4x56u3)',
            'option_a': 'To show company debts',
            'option_b': 'To verify that debits equal credits',
            'option_c': 'To increase revenue',
            'option_d': 'To reduce taxes',
            'correct_option': 'B'
        },
        {
            'question_text': 'What does a cash flow statement show? (kwzh0v59)',
            'option_a': 'Cash inflows and outflows',
            'option_b': 'Company assets',
            'option_c': 'Company debts',
            'option_d': 'Company profit',
            'correct_option': 'A'
        },
        {
            'question_text': 'In accrual accounting, when is revenue recorded? (yx6gsv4o)',
            'option_a': 'When cash is received',
            'option_b': 'When earned, even if cash is not yet received',
            'option_c': 'At year-end',
            'option_d': 'When expense occurs',
            'correct_option': 'B'
        },
        {
            'question_text': 'What are prepaid expenses? (zw88tp4r)',
            'option_a': 'Expenses paid in advance but not yet incurred',
            'option_b': 'Payables',
            'option_c': 'Revenue',
            'option_d': 'Loss',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is accounts receivable? (wxq5zzkm)',
            'option_a': 'Company debt',
            'option_b': 'Amount to be received by the company',
            'option_c': 'Company profit',
            'option_d': 'Company expenses',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is accounts payable? (hx0yyp1y)',
            'option_a': 'Receivables',
            'option_b': 'Company’s obligations or payables',
            'option_c': 'Company profit',
            'option_d': 'Company assets',
            'correct_option': 'B'
        },
        {
            'question_text': 'What does depreciation represent? (ww079n17)',
            'option_a': 'Reduction in asset value',
            'option_b': 'Company profit',
            'option_c': 'Cash inflow',
            'option_d': 'Debt',
            'correct_option': 'A'
        },
        {
            'question_text': 'What does inventory represent? (fx468nn4)',
            'option_a': 'Company assets',
            'option_b': 'Company stock or goods',
            'option_c': 'Cash',
            'option_d': 'Debts',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the first step in making a journal entry? (vx0i9mt8)',
            'option_a': 'Posting to ledger',
            'option_b': 'Recording the transaction',
            'option_c': 'Preparing trial balance',
            'option_d': 'Preparing cash flow statement',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is a general ledger? (twv8h8h3)',
            'option_a': 'Collection of all accounting records',
            'option_b': 'Only cash accounts',
            'option_c': 'Only revenue accounts',
            'option_d': 'Only expense accounts',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the accounting equation? (iw4797pu)',
            'option_a': 'Assets = Liabilities + Equity',
            'option_b': 'Assets = Income + Expenses',
            'option_c': 'Income = Revenue – Expenses',
            'option_d': 'Liabilities = Assets – Expenses',
            'correct_option': 'A'
        },
        {
            'question_text': 'How long is a financial year? (fx989oj8)',
            'option_a': '6 months',
            'option_b': '12 months',
            'option_c': '3 months',
            'option_d': '24 months',
            'correct_option': 'B'
        },
        {
            'question_text': 'When are adjusting entries made? (vx2n13vm)',
            'option_a': 'Immediately after transaction',
            'option_b': 'Before preparing financial statements',
            'option_c': 'After cash flow statement',
            'option_d': 'After ledger posting',
            'correct_option': 'B'
        },
        {
            'question_text': 'What are accrued expenses? (ww48974m)',
            'option_a': 'Expenses incurred but not yet paid',
            'option_b': 'Prepaid expenses',
            'option_c': 'Payables',
            'option_d': 'Company assets',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the purpose of bank reconciliation? (wx5601n9)',
            'option_a': 'To record cash',
            'option_b': 'To reconcile differences between bank and company accounts',
            'option_c': 'To pay taxes',
            'option_d': 'To increase profit',
            'correct_option': 'B'
        },
        {
            'question_text': 'When are closing entries made? (kxpy53l2)',
            'option_a': 'After every transaction',
            'option_b': 'At the end of the financial year',
            'option_c': 'After cash flow statement',
            'option_d': 'During ledger posting',
            'correct_option': 'B'
        },
        {
            'question_text': 'Which financial statement shows the company’s financial position? (mxf0630m)',
            'option_a': 'Income Statement',
            'option_b': 'Balance Sheet',
            'option_c': 'Cash Flow Statement',
            'option_d': 'Trial Balance',
            'correct_option': 'B'
        },
    ],

    'AC Technician': [
        {
            'question_text': 'What does HVAC stand for? (xxv3po35)',
            'option_a': 'High Voltage Air Control',
            'option_b': 'Heating, Ventilation, and Air Conditioning',
            'option_c': 'Heavy Vacuum Air Cooler',
            'option_d': 'Heat Valve Automatic Control',
            'correct_option': 'B'
        },
        {
            'question_text': 'If an AC is not cooling properly, what should be checked first? (fwx3272e)',
            'option_a': 'Electrical connection',
            'option_b': 'Compressor',
            'option_c': 'Fan',
            'option_d': 'Filter',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the purpose of refrigerant in an AC? (ux57s6w7)',
            'option_a': 'To heat the air',
            'option_b': 'To absorb heat and produce cool air',
            'option_c': 'To save electricity',
            'option_d': 'To remove water',
            'correct_option': 'B'
        },
        {
            'question_text': 'If water is dripping from the AC, what could be the possible cause? (vx29q0mn)',
            'option_a': 'Dirty filter',
            'option_b': 'Blocked drain pipe',
            'option_c': 'Faulty compressor',
            'option_d': 'Excess refrigerant',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the function of a thermostat in an AC system? (kw2m8jyk)',
            'option_a': 'To control temperature',
            'option_b': 'To save electricity',
            'option_c': 'To clean the air',
            'option_d': 'To drain water',
            'correct_option': 'A'
        },
        {
            'question_text': 'How often should AC filters be cleaned? (hy8zpe63)',
            'option_a': 'Daily',
            'option_b': 'Weekly',
            'option_c': 'Monthly or as needed',
            'option_d': 'Never',
            'correct_option': 'C'
        },
        {
            'question_text': 'If the compressor is running but the fan is not, what should be done? (gxkun3g2)',
            'option_a': 'Turn off the system',
            'option_b': 'Check fan wiring and motor',
            'option_c': 'Add more refrigerant',
            'option_d': 'Do nothing',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the purpose of the indoor unit in a split AC? (lx9q80e8)',
            'option_a': 'To expel heat',
            'option_b': 'To deliver cool air inside',
            'option_c': 'To remove water',
            'option_d': 'To save electricity',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is a key component of the outdoor unit? (nxy91v16)',
            'option_a': 'Fan',
            'option_b': 'Compressor',
            'option_c': 'Condenser',
            'option_d': 'Thermostat',
            'correct_option': 'B'
        },
        {
            'question_text': 'How can refrigerant leaks in an AC be detected? (nxf173e1)',
            'option_a': 'By the smell of air',
            'option_b': 'Using a special leak detector',
            'option_c': 'By compressor sound',
            'option_d': 'By dripping water',
            'correct_option': 'B'
        },
        {
            'question_text': 'How can the efficiency of an AC be improved? (vz0pf46f)',
            'option_a': 'Keep doors and windows closed',
            'option_b': 'Keep filters clean',
            'option_c': 'Maintain proper refrigerant levels',
            'option_d': 'All of the above',
            'correct_option': 'D'
        },
        {
            'question_text': 'What could be the cause of high pressure in an AC system? (mx88y157)',
            'option_a': 'Faulty fan',
            'option_b': 'Dirty condenser',
            'option_c': 'Low refrigerant',
            'option_d': 'Compressor off',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the function of the evaporator coil in an AC? (twy4em99)',
            'option_a': 'To absorb heat and cool the air',
            'option_b': 'To remove water',
            'option_c': 'To operate the compressor',
            'option_d': 'To save electricity',
            'correct_option': 'A'
        },
        {
            'question_text': 'Which tool is essential for AC service? (mx37mos2)',
            'option_a': 'Screwdriver',
            'option_b': 'Manifold Gauge Set',
            'option_c': 'Hammer',
            'option_d': 'Wrench',
            'correct_option': 'B'
        },
        {
            'question_text': 'If an AC compressor burns out, what should be done? (uxx4m70p)',
            'option_a': 'Only clean the filter',
            'option_b': 'Replace the compressor',
            'option_c': 'Do nothing',
            'option_d': 'Just refill refrigerant',
            'correct_option': 'B'
        },
        {
            'question_text': 'Why is R-22 being replaced with R-410A in AC systems? (ox92ui00)',
            'option_a': 'For better cooling',
            'option_b': 'Because it is environmentally friendly',
            'option_c': 'To save electricity',
            'option_d': 'To strengthen the compressor',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the function of the capillary tube in an AC? (ywup9131)',
            'option_a': 'To control refrigerant flow and pressure',
            'option_b': 'To operate the fan',
            'option_c': 'To drain water',
            'option_d': 'To shut off the compressor',
            'correct_option': 'A'
        },
        {
            'question_text': 'Why does the indoor unit of a split AC accumulate more dust? (yzz31476)',
            'option_a': 'Due to fan operation',
            'option_b': 'Less filtration',
            'option_c': 'Dust enters with air',
            'option_d': 'All of the above',
            'correct_option': 'D'
        },
        {
            'question_text': 'What is most important for safety during AC maintenance? (oxo96t0k)',
            'option_a': 'Turn off water',
            'option_b': 'Turn off electricity',
            'option_c': 'Remove refrigerant',
            'option_d': 'Stop compressor',
            'correct_option': 'B'
        },
        {
            'question_text': 'What does “dehumidification” mean in an AC system? (nx21yjk7)',
            'option_a': 'To heat the air',
            'option_b': 'To reduce humidity',
            'option_c': 'To produce water',
            'option_d': 'To increase fan speed',
            'correct_option': 'B'
        },
        {
            'question_text': 'What happens if the AC thermostat malfunctions? (qxm1s6rt)',
            'option_a': 'Very close',
            'option_b': 'At manufacturer-recommended distance',
            'option_c': 'Anywhere',
            'option_d': 'As near as possible',
            'correct_option': 'B'
        },
        {
            'question_text': 'How can AC noise be reduced? (swr6tijh)',
            'option_a': 'Clean fan and check motor',
            'option_b': 'Replace compressor',
            'option_c': 'Do not change filters',
            'option_d': 'No action required',
            'correct_option': 'A'
        },
        {
            'question_text': 'How can the lifespan of an AC compressor be increased? (lz4ei3e8)',
            'option_a': 'Proper maintenance',
            'option_b': 'Clean filters',
            'option_c': 'Maintain correct refrigerant level',
            'option_d': 'All of the above',
            'correct_option': 'D'
        },
    ],

    'Draftsman': [
        {
            'question_text': 'Which software is most commonly used by draftsmen for creating 2D drawings? (ex3u1836)',
            'option_a': 'Revit',
            'option_b': 'AutoCAD',
            'option_c': 'SketchUp',
            'option_d': 'SolidWorks',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the standard paper size used for engineering drawings in the Gulf region? (ey9836p2)',
            'option_a': 'A2',
            'option_b': 'A3',
            'option_c': 'A1',
            'option_d': 'A4',
            'correct_option': 'C'
        },
        {
            'question_text': 'What is the purpose of layer management in AutoCAD? (qx98wevz)',
            'option_a': 'To color drawings',
            'option_b': 'To organize different elements separately',
            'option_c': 'To reduce file size',
            'option_d': 'To improve 3D modeling',
            'correct_option': 'B'
        },
        {
            'question_text': 'In an architectural drawing, what does “FFL” stand for? (px47z6fo)',
            'option_a': 'Radius',
            'option_b': 'Diameter',
            'option_c': 'Circumference',
            'option_d': 'Angle',
            'correct_option': 'B'
        },
        {
            'question_text': 'What does the scale 1:100 mean in drafting? (mwt3t4vn)',
            'option_a': '1 unit on drawing = 100 units in real life',
            'option_b': '100 units on drawing = 1 unit in real life',
            'option_c': 'Drawing and real life are same size',
            'option_d': 'None of these',
            'correct_option': 'A'
        },
        {
            'question_text': 'Which line type represents a hidden edge in technical drawings? (hx30t75u)',
            'option_a': 'Continuous thick line',
            'option_b': 'Dashed line',
            'option_c': 'Chain line',
            'option_d': 'Center line',
            'correct_option': 'B'
        },
        {
            'question_text': 'What command is used in AutoCAD to create parallel lines? (fwql513t)',
            'option_a': 'OFFSET',
            'option_b': 'ARRAY',
            'option_c': 'COPY',
            'option_d': 'MIRROR',
            'correct_option': 'A'
        },
        {
            'question_text': 'Which projection is most commonly used in engineering drawings? (zyu4l973)',
            'option_a': 'Isometric projection',
            'option_b': 'Oblique projection',
            'option_c': 'Orthographic projection',
            'option_d': 'Perspective projection',
            'correct_option': 'C'
        },
        {
            'question_text': 'What is the function of the “Trim” command in AutoCAD? (hw3w31p5)',
            'option_a': 'To cut unwanted portions',
            'option_b': 'To copy objects',
            'option_c': 'To extend lines',
            'option_d': 'To offset elements',
            'correct_option': 'A'
        },
        {
            'question_text': 'In a piping layout drawing, what does “NPS” mean? (vw283yky)',
            'option_a': 'Nominal Pipe Size',
            'option_b': 'New Piping System',
            'option_c': 'Net Pipe Strength',
            'option_d': 'None of these',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the unit usually used for dimensions in architectural drawings? (oz3w15yg)',
            'option_a': 'Millimeters',
            'option_b': 'Centimeters',
            'option_c': 'Inches',
            'option_d': 'Feet and Inches',
            'correct_option': 'D'
        },
        {
            'question_text': 'What is the use of the "Hatch" command in AutoCAD? (pxv91k8u)',
            'option_a': 'To draw text',
            'option_b': 'To fill closed areas with patterns',
            'option_c': 'To make dimensions',
            'option_d': 'To copy layers',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the full form of HVAC drawings? (lw565rki)',
            'option_a': 'Heating, Ventilation and Air Conditioning',
            'option_b': 'Hydraulic, Vacuum and Air Control',
            'option_c': 'High Voltage Air Circulation',
            'option_d': 'None of these',
            'correct_option': 'A'
        },
        {
            'question_text': 'What does a section drawing represent? (nxlwp7k0)',
            'option_a': 'Outer appearance',
            'option_b': 'Interior details cut through an object',
            'option_c': '3D visualization',
            'option_d': 'Site layout',
            'correct_option': 'B'
        },
        {
            'question_text': 'What command is used to join two lines in AutoCAD? (uw0s0481)',
            'option_a': 'Top of Concrete',
            'option_b': 'Type of Column',
            'option_c': 'Thickness of Ceiling',
            'option_d': 'Total Overall Cost',
            'correct_option': 'A'
        },
        {
            'question_text': 'Which file extension is standard for AutoCAD drawings? (pxrly7k5)',
            'option_a': '.DXF',
            'option_b': '.DWG',
            'option_c': '.CAD',
            'option_d': '.DWF',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the purpose of “Dimensioning” in a drawing?  (sxe67z54)',
            'option_a': 'Decoration',
            'option_b': 'Measurement communication',
            'option_c': 'Scaling',
            'option_d': 'Printing',
            'correct_option': 'B'
        },
        {
            'question_text': 'Which coordinate system does AutoCAD use? (nwq014n6)',
            'option_a': 'Reinforced Cement Concrete',
            'option_b': 'Rectangular Concrete Column',
            'option_c': 'Ready Cement Construction',
            'option_d': 'Raw Cement Compound',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the use of “XREF” in AutoCAD? (qwk61oqj)',
            'option_a': 'To reference external drawings',
            'option_b': 'To export file',
            'option_c': 'To edit dimensions',
            'option_d': 'To delete layers',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the main advantage of using layers in CAD drawings? (rxn7oys6)',
            'option_a': 'To make drawings colorful',
            'option_b': 'To separate elements logically',
            'option_c': 'To reduce drawing size',
            'option_d': 'To increase print speed',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the default unit in AutoCAD when drawing architectural plans? (wzoxrwk3)',
            'option_a': 'Inches',
            'option_b': 'Millimeters',
            'option_c': 'Feet',
            'option_d': 'Depends on user settings',
            'correct_option': 'D'
        },
        {
            'question_text': 'What is the purpose of using a title block? (wxjoq5z0)',
            'option_a': 'To add decorative borders',
            'option_b': 'To show drawing information like name, scale, and date',
            'option_c': 'To increase drawing size',
            'option_d': 'To make drawing printable',
            'correct_option': 'B'
        },
    ],

    'Bike Rider': [
        {
            'question_text': 'What is the main responsibility of a delivery bike rider? (hx85lzfj)',
            'option_a': 'To reach office on time',
            'option_b': 'To deliver items safely and on schedule',
            'option_c': 'To wash the bike',
            'option_d': 'To repair the engine',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should a rider check before starting the bike every day? (swgszw72)',
            'option_a': 'Headlight, brake, indicators, and fuel',
            'option_b': 'Only tyre pressure',
            'option_c': 'Only mirror',
            'option_d': 'None',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the most important safety gear for a rider? (ex2gq55m)',
            'option_a': 'Gloves',
            'option_b': 'Helmet',
            'option_c': 'Jacket',
            'option_d': 'Sunglasses',
            'correct_option': 'B'
        },
        {
            'question_text': 'What does the red traffic light mean? (nxpx50kg)',
            'option_a': 'Go fast',
            'option_b': 'Stop',
            'option_c': 'Slow down',
            'option_d': 'Turn left',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should you do if your bike skids on a wet road? (rx05t3x4)',
            'option_a': 'Apply both brakes hard',
            'option_b': 'Leave the accelerator slowly and control balance',
            'option_c': 'Turn suddenly',
            'option_d': 'Jump off the bike',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the legal minimum age for bike riders in Gulf countries (average)? (ixn2k7wy)',
            'option_a': '16',
            'option_b': '18',
            'option_c': '20',
            'option_d': '21',
            'correct_option': 'B'
        },
        {
            'question_text': 'Why should you not use a mobile phone while riding? (uxm9l35o)',
            'option_a': 'It looks unprofessional',
            'option_b': 'It can distract and cause accidents',
            'option_c': 'It is not allowed by the company',
            'option_d': 'None',
            'correct_option': 'B'
        },
        {
            'question_text': 'If your delivery location is not clear, what should you do? (oxg9n02t)',
            'option_a': 'Guess and go anywhere',
            'option_b': 'Call the customer or company for confirmation',
            'option_c': 'Cancel the delivery',
            'option_d': 'Wait on the road',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the purpose of engine oil in a bike? (vxtfh4yu)',
            'option_a': 'Decoration',
            'option_b': 'Cooling and lubrication',
            'option_c': 'Speed control',
            'option_d': 'To make noise',
            'correct_option': 'B'
        },
        {
            'question_text': 'What document must you always carry while riding? (gw0f61m7)',
            'option_a': 'Driving license',
            'option_b': 'CV',
            'option_c': 'Passport',
            'option_d': 'None',
            'correct_option': 'A'
        },
        {
            'question_text': 'What should you do in case of a small road accident? (lx58x04t)',
            'option_a': 'Run away',
            'option_b': 'Inform supervisor and traffic police',
            'option_c': 'Shout at the other driver',
            'option_d': 'Ignore and go',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the safe distance between two moving bikes? (fxwvw0fr)',
            'option_a': '1 meter',
            'option_b': '3–5 meters',
            'option_c': '10 meters',
            'option_d': 'None',
            'correct_option': 'B'
        },
        {
            'question_text': 'What does “Defensive Driving” mean? (xx36g6x8)',
            'option_a': 'Driving very fast',
            'option_b': 'Driving safely and predicting others’ mistakes',
            'option_c': 'Ignoring signals',
            'option_d': 'Overtaking every time',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should be checked in bike tires daily? (lxj5toen)',
            'option_a': 'Colour',
            'option_b': 'Air pressure and tread condition',
            'option_c': 'Size',
            'option_d': 'None',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the normal fuel used in most delivery bikes? (ix968138)',
            'option_a': 'Diesel',
            'option_b': 'Petrol',
            'option_c': 'Gas',
            'option_d': 'Kerosene',
            'correct_option': 'B'
        },
        {
            'question_text': 'When should a rider use hazard lights? (qw38g679)',
            'option_a': 'During breakdown or emergency',
            'option_b': 'At red signal',
            'option_c': 'During rain',
            'option_d': 'Always',
            'correct_option': 'A'
        },
        {
            'question_text': 'What should you do if your bike stops in the middle of the road? (zxlhso1k)',
            'option_a': 'Leave it there',
            'option_b': 'Move it to the side and check the problem',
            'option_c': 'Wait for someone',
            'option_d': 'Keep pressing the horn',
            'correct_option': 'B'
        },
        {
            'question_text': 'How can you save fuel during delivery? (lw5gu543)',
            'option_a': 'Ride at steady speed',
            'option_b': 'Accelerate fast',
            'option_c': 'Ride in low gear always',
            'option_d': 'Stop frequently',
            'correct_option': 'A'
        },
        {
            'question_text': 'What should you do before overtaking another vehicle? (yw1k998p)',
            'option_a': 'Blow horn and check mirror',
            'option_b': 'Just speed up',
            'option_c': 'Overtake from right always',
            'option_d': 'Close eyes',
            'correct_option': 'A'
        },
        {
            'question_text': 'What should be done after every 1000–1500 km ride? (mxi2fs68)',
            'option_a': 'Change helmet',
            'option_b': 'Service the bike (oil, brakes, chain)',
            'option_c': 'Paint the bike',
            'option_d': 'None',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the correct hand signal for turning left? (pxsio3kx)',
            'option_a': 'Right hand straight',
            'option_b': 'Left hand straight',
            'option_c': 'Hand down',
            'option_d': 'None',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the importance of GPS in delivery work? (rx2i5s51)',
            'option_a': 'For entertainment',
            'option_b': 'To track routes and deliveries accurately',
            'option_c': 'To check messages',
            'option_d': 'None',
            'correct_option': 'B'
        },
        {
            'question_text': 'When riding at night, what is most important? (uw2ny6y1)',
            'option_a': 'Use headlight',
            'option_b': 'Ride fast',
            'option_c': 'Horn continuously',
            'option_d': 'Remove helmet',
            'correct_option': 'A'
        },
        {
            'question_text': 'What should you do if the weather is too hot? (kxw8v355)',
            'option_a': 'Don’t wear helmet',
            'option_b': 'Stay hydrated and take breaks',
            'option_c': 'Ride faster',
            'option_d': 'Ignore company rules',
            'correct_option': 'B'
        },
        {
            'question_text': 'If your supervisor gives wrong location, what should you do? (ux29oeep)',
            'option_a': 'Argue',
            'option_b': 'Politely confirm and clarify',
            'option_c': 'Cancel delivery',
            'option_d': 'Ignore the order',
            'correct_option': 'B'
        },
    ],

    'Heavy Truck Driver': [
        {
            'question_text': 'What is the most important responsibility of a heavy truck driver? (px49pr26)',
            'option_a': 'Cleaning the vehicle',
            'option_b': 'Delivering goods safely and on time',
            'option_c': 'Driving fast on the road',
            'option_d': 'Competing with other drivers',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the most important check before driving a truck? (mw719r24)',
            'option_a': 'Engine oil, brakes, tire pressure, and lights',
            'option_b': 'Only fuel',
            'option_c': 'Only brakes',
            'option_d': 'Nothing',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the most important safety item for a driver? (fxs0w420)',
            'option_a': 'Helmet',
            'option_b': 'Seat belt',
            'option_c': 'Gloves',
            'option_d': 'Jacket',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should you do if a truck tire bursts? (lwtl61fn)',
            'option_a': 'Stop immediately and move to the side',
            'option_b': 'Keep driving without slowing down',
            'option_c': 'Do not apply brakes immediately',
            'option_d': 'Abandon the truck',
            'correct_option': 'A'
        },
        {
            'question_text': 'What does a red traffic light mean? (wx595pg7)',
            'option_a': 'Drive fast',
            'option_b': 'Stop',
            'option_c': 'Drive slowly',
            'option_d': 'Turn left',
            'correct_option': 'B'
        },
        {
            'question_text': 'During long drives, when should you take a break? (lw57671w)',
            'option_a': 'Every 2–3 hours',
            'option_b': 'Never',
            'option_c': 'Every 6 hours',
            'option_d': 'Only in the evening',
            'correct_option': 'A'
        },
        {
            'question_text': 'What should you do if the truck load is swinging? (vxznn7kw)',
            'option_a': 'Drive fast',
            'option_b': 'Reduce speed and apply brakes gently',
            'option_c': 'Turn off the engine',
            'option_d': 'Unload the goods',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should you do if the truck’s front brakes fail? (lw82xq15)',
            'option_a': 'Use rear brakes and slow down gradually',
            'option_b': 'Drive fast',
            'option_c': 'Turn left',
            'option_d': 'Do nothing',
            'correct_option': 'A'
        },
        {
            'question_text': 'Why do we check engine oil and coolant? (lx18ujmt)',
            'option_a': 'To keep the vehicle clean',
            'option_b': 'To keep the engine cool and safe',
            'option_c': 'To increase speed',
            'option_d': 'Only for the company',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should you do during heavy rain? (nw12p1mp)',
            'option_a': 'Reduce speed',
            'option_b': 'Drive at normal speed',
            'option_c': 'Only honk',
            'option_d': 'Do nothing',
            'correct_option': 'A'
        },
        {
            'question_text': 'Why is proper loading of truck goods important? (xxiyn935)',
            'option_a': 'To keep weight low',
            'option_b': 'To reduce pressure on tires and brakes',
            'option_c': 'Only for the driver',
            'option_d': 'To keep the vehicle clean',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should you do if the truck breaks down on the highway? (pwi12p85)',
            'option_a': 'Immediately move to the side',
            'option_b': 'Leave it on the road',
            'option_c': 'Block traffic',
            'option_d': 'Blame others',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the most important thing for night driving? (uwnqimv8)',
            'option_a': 'Headlights and reflectors',
            'option_b': 'Drive fast',
            'option_c': 'Keep honking',
            'option_d': 'Increase engine sound',
            'correct_option': 'A'
        },
        {
            'question_text': 'What does “Defensive Driving” mean? (tx3f90t1)',
            'option_a': 'Driving very fast',
            'option_b': 'Being cautious and anticipating other drivers’ mistakes',
            'option_c': 'Overtaking frequently',
            'option_d': 'Standing on the side of the road',
            'correct_option': 'B'
        },
        {
            'question_text': 'When should you test the brakes? (nw35f15m)',
            'option_a': 'Every day before driving',
            'option_b': 'Once a week',
            'option_c': 'Once a month',
            'option_d': 'Never',
            'correct_option': 'A'
        },
        {
            'question_text': 'What should you do if the truck gear gets locked? (ux4g9y0z)',
            'option_a': 'Immediately put it in reverse',
            'option_b': 'Turn off the engine and check',
            'option_c': 'Drive fast',
            'option_d': 'Honk continuously',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should you do if there is traffic jam on the highway? (mx8g9f13)',
            'option_a': 'Leave the vehicle',
            'option_b': 'Wait calmly and follow traffic rules',
            'option_c': 'Overtake',
            'option_d': 'Keep honking',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should you eat or drink during long drives? (zxpuo0r1)',
            'option_a': 'Fatty food',
            'option_b': 'Light food and water',
            'option_c': 'Nothing',
            'option_d': 'Only coffee',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should you do if involved in an accident? (zx0pm2wv)',
            'option_a': 'Run away',
            'option_b': 'Inform the police and supervisor',
            'option_c': 'Blame others',
            'option_d': 'Do nothing',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the consequence of violating traffic rules? (hw056zgi)',
            'option_a': 'Only a fine',
            'option_b': 'Accident and fine',
            'option_c': 'Only loss',
            'option_d': 'Nothing',
            'correct_option': 'A'
        },
        {
            'question_text': 'When should truck servicing be done? (ow309mly)',
            'option_a': 'Every 5000–10000 km',
            'option_b': 'Never',
            'option_c': 'Every month',
            'option_d': 'Only if brakes fail',
            'correct_option': 'A'
        },
        {
            'question_text': 'What should you do if rear lights are not working? (jxvv8lre)',
            'option_a': 'Only use front lights',
            'option_b': 'Repair immediately',
            'option_c': 'Drive fast',
            'option_d': 'Do nothing',
            'correct_option': 'B'
        },
        {
            'question_text': 'What does “Load Securing” mean? (kw99fi0k)',
            'option_a': 'Properly tying and securing goods',
            'option_b': 'Lifting goods',
            'option_c': 'Dropping goods',
            'option_d': 'Watching goods',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the most important skill for a driver? (vx166313)',
            'option_a': 'Driving fast',
            'option_b': 'Caution and punctuality',
            'option_c': 'Only keeping the truck clean',
            'option_d': 'Remembering the route',
            'correct_option': 'B'
        },
        {
            'question_text': 'If the company asks you to carry double load, what should you do? (hx2k8m0q)',
            'option_a': 'Yes, without checking',
            'option_b': 'First check legal limits and truck capacity',
            'option_c': 'Refuse',
            'option_d': 'Place goods haphazardly',
            'correct_option': 'B'
        },
    ],

    'Construction Helper': [
        {
            'question_text': 'What is the common cement-to-sand ratio for plaster? (uyo027u1)',
            'option_a': '1:1',
            'option_b': '1:2',
            'option_c': '1:4',
            'option_d': '1:6',
            'correct_option': 'C'
        },
        {
            'question_text': 'What does "Curing" mean? (tx83r2t5)',
            'option_a': 'Breaking concrete',
            'option_b': 'Making concrete strong with moisture',
            'option_c': 'Mixing concrete',
            'option_d': 'Pouring concrete',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is "Rebar"? (lx8y1556)',
            'option_a': 'Wood',
            'option_b': 'Steel rod',
            'option_c': 'Stone',
            'option_d': 'Plastic pipe',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is "Plumb bob" used for? (mx02e5sg)',
            'option_a': 'Checking horizontal level',
            'option_b': 'Checking vertical alignment',
            'option_c': 'For mixing',
            'option_d': 'For finishing',
            'correct_option': 'B'
        },
        {
            'question_text': 'What happens if too much water is added to concrete? (sxs774tx)',
            'option_a': 'Concrete becomes stronger',
            'option_b': 'Concrete becomes weak and crumbly',
            'option_c': 'Color improves',
            'option_d': 'Nothing happens',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is "Formwork"? (hx4p8trj)',
            'option_a': 'Ladder',
            'option_b': 'Temporary wood or mold used to shape concrete',
            'option_c': 'Worker\'s equipment',
            'option_d': 'Steel frame',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is "Slab"? (xx84je83)',
            'option_a': 'Wall',
            'option_b': 'Concrete plate for floor or roof',
            'option_c': 'Door',
            'option_d': 'Pillar',
            'correct_option': 'B'
        },
        {
            'question_text': 'If the supervisor asks you to check the level, what will you use? (uxp0her1)',
            'option_a': 'Plumb bob',
            'option_b': 'Spirit level',
            'option_c': 'Wheelbarrow',
            'option_d': 'Hammer',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is "Mortar"? (uwik5xwn)',
            'option_a': 'Cement + sand + water',
            'option_b': 'Cement + gravel',
            'option_c': 'Sand + stones',
            'option_d': 'Gravel + water',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is included in PPE (Personal Protective Equipment)? (exv4j7fi)',
            'option_a': 'Clothes, turban',
            'option_b': 'Helmet, gloves, safety shoes, goggles',
            'option_c': 'Shoes and shirt',
            'option_d': 'Watch only',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the purpose of a "Concrete Vibrator"? (yx1hgxv3)',
            'option_a': 'To soften the mix',
            'option_b': 'To remove air bubbles and strengthen concrete',
            'option_c': 'To make colour shine',
            'option_d': 'To test strength',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the most important safety rule during scaffolding work? (xx47k0s3)',
            'option_a': 'Climb fast',
            'option_b': 'Always wear a safety harness',
            'option_c': 'Go barefoot',
            'option_d': 'Practice climbing',
            'correct_option': 'B'
        },
        {
            'question_text': 'What does "Excavation" mean? (qws1ji65)',
            'option_a': 'Digging the ground',
            'option_b': 'Painting walls',
            'option_c': 'Installing doors',
            'option_d': 'Plastering',
            'correct_option': 'A'
        },
        {
            'question_text': 'If a gas pipe is visible during excavation, what should you do? (mxszo0tx)',
            'option_a': 'Continue work',
            'option_b': 'Inform supervisor immediately and clear the area',
            'option_c': 'Remove by hand',
            'option_d': 'Paint over it',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the purpose of "Tying Steel"? (hw1ot62y)',
            'option_a': 'To tie steel rods firmly',
            'option_b': 'For painting',
            'option_c': 'To remove soil',
            'option_d': 'To test quality',
            'correct_option': 'A'
        },
        {
            'question_text': 'Where is "Bitumen" used? (gx6sez53)',
            'option_a': 'On walls',
            'option_b': 'For road construction',
            'option_c': 'For drinking water',
            'option_d': 'In plaster',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the purpose of a "Barricade"? (xwh59v6l)',
            'option_a': 'To block or secure an area',
            'option_b': 'To provide shade',
            'option_c': 'To place tools',
            'option_d': 'To transport materials',
            'correct_option': 'A'
        },
        {
            'question_text': 'When should site cleaning be done? (rxvofizf)',
            'option_a': 'Only in the morning',
            'option_b': 'At the end of the day or when required',
            'option_c': 'Once a week',
            'option_d': 'Never',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should be done if electricity goes off while pouring concrete? (mxfn0ni8)',
            'option_a': 'Leave the mix',
            'option_b': 'Finish quickly or level manually',
            'option_c': 'Pour water',
            'option_d': 'Stop immediately',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is checked during “Surveying”? (ox942v44)',
            'option_a': 'Level, angle, and height',
            'option_b': 'Colour',
            'option_c': 'Meal time',
            'option_d': 'S',
            'correct_option': 'B'
        },
        {
            'question_text': 'Why is a “Safety Meeting” held? (pxqyw0x5)',
            'option_a': 'To remind workers about safety rules',
            'option_b': 'To assign work',
            'option_c': 'Just formal discussion',
            'option_d': 'T',
            'correct_option': 'B'
        },
        {
            'question_text': 'If the supervisor is not present, who makes the decision? (qx3n50zh)',
            'option_a': 'Senior worker or team leader',
            'option_b': 'Anyone',
            'option_c': 'New worker',
            'option_d': 'N',
            'correct_option': 'B'
        },
    ],

    'Driver': [
        {
            'question_text': 'What is meant by "Defensive Driving"? (nxzfv9jv)',
            'option_a': 'Driving with aggression',
            'option_b': 'Driving with full concentration and anticipation',
            'option_c': 'Using the mobile phone while driving',
            'option_d': 'Late night driving',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should you do if a vehicle is approaching from the opposite direction on a narrow road? (yx96ishz)',
            'option_a': 'Keep driving fast',
            'option_b': 'Slow down and move your vehicle to the side',
            'option_c': 'Keep moving slowly',
            'option_d': 'Stop completely',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should you do before starting your car? (exfslu9p)',
            'option_a': 'Wait for a week',
            'option_b': 'Check your vehicle beforehand',
            'option_c': 'It\'s not necessary',
            'option_d': 'Never check',
            'correct_option': 'B'
        },
        {
            'question_text': 'Which documents must a driver always keep with him? (ky3xu5n0)',
            'option_a': 'License only',
            'option_b': 'ID card and license',
            'option_c': 'Registration, insurance, and license',
            'option_d': 'Passport only',
            'correct_option': 'C'
        },
        {
            'question_text': 'Before changing lanes, what must a driver do? (hx650sho)',
            'option_a': 'Blow the horn',
            'option_b': 'Use the indicator and check mirrors',
            'option_c': 'Wait for an hour',
            'option_d': 'Move immediately',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should be the minimum safe distance between two vehicles? (zx76nn42)',
            'option_a': '1 meter',
            'option_b': '3 seconds',
            'option_c': '10 meters',
            'option_d': 'No distance needed',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should you do if you feel sleepy while driving? (tx876643)',
            'option_a': 'Keep drinking water',
            'option_b': 'Stop the car and take some rest',
            'option_c': 'Finish driving quickly',
            'option_d': 'Use music loudly',
            'correct_option': 'B'
        },
        {
            'question_text': 'What ensures the safety of both driver and passengers? (gw9706iy)',
            'option_a': 'Obeying traffic laws and driving attentively',
            'option_b': 'Driving fast',
            'option_c': 'Talking on the phone while driving',
            'option_d': 'Loud music',
            'correct_option': 'A'
        },
        {
            'question_text': 'What should a driver do if an accident happens? (vyrlrz64)',
            'option_a': 'Run away',
            'option_b': 'Argue with the other driver',
            'option_c': 'Inform the police and provide help',
            'option_d': 'Keep driving',
            'correct_option': 'C'
        },
        {
            'question_text': 'How can a driver keep their vehicle in good condition? (kw3f73le)',
            'option_a': 'Regular maintenance and checking',
            'option_b': 'Ignore small problems',
            'option_c': 'Drive without care',
            'option_d': 'Only wash outside',
            'correct_option': 'A'
        },
        {
            'question_text': 'Why do you want to work as a driver? (uwzjtv08)',
            'option_a': 'Better salary and career opportunities',
            'option_b': 'For fame',
            'option_c': 'To travel freely',
            'option_d': 'For fun only',
            'correct_option': 'A'
        },
        {
            'question_text': 'What happens if a driver consumes alcohol before driving? (pxeh0zje)',
            'option_a': 'Speed increases',
            'option_b': 'Vision and reaction slow down',
            'option_c': 'Becomes more alert',
            'option_d': 'Sight improves',
            'correct_option': 'B'
        },
        {
            'question_text': 'When should you overtake another vehicle? (yyr1eilv)',
            'option_a': 'Whenever you want',
            'option_b': 'When no vehicle is ahead',
            'option_c': 'On an empty road',
            'option_d': 'Only at night',
            'correct_option': 'C'
        },
        {
            'question_text': 'What should you do when you need to stop a vehicle suddenly? (ry7er0v4)',
            'option_a': 'Never press the brake suddenly',
            'option_b': 'Reverse immediately',
            'option_c': 'Slow down gradually and then stop',
            'option_d': 'Slam the brakes',
            'correct_option': 'C'
        },
        {
            'question_text': 'What should you do if you get a speeding ticket? (hyw9rkq1)',
            'option_a': 'Argue with the officer',
            'option_b': 'Make excuses',
            'option_c': 'Accept responsibility and apologize',
            'option_d': 'Ignore it',
            'correct_option': 'C'
        },
        {
            'question_text': 'What should you do if your headlights fail at night? (rw4177o4)',
            'option_a': 'Stop immediately',
            'option_b': 'Remember the way and drive slowly',
            'option_c': 'Ignore and keep driving',
            'option_d': 'Speed up',
            'correct_option': 'A'
        },
        {
            'question_text': 'What should you do if you see an accident while driving? (xwj412nw)',
            'option_a': 'Inform the police and help',
            'option_b': 'Leave the place quickly',
            'option_c': 'Record a video',
            'option_d': 'Ignore it',
            'correct_option': 'A'
        },
        {
            'question_text': 'Why is wearing a seat belt important? (zxo87x3j)',
            'option_a': 'It\'s a legal requirement',
            'option_b': 'For safety',
            'option_c': 'For beauty',
            'option_d': 'For fashion',
            'correct_option': 'B'
        },
        {
            'question_text': 'What items should be in a car\'s emergency kit? (zxqutmv2)',
            'option_a': 'License only',
            'option_b': 'Torch, jack, first aid box',
            'option_c': 'Water bottle',
            'option_d': 'Clothes only',
            'correct_option': 'B'
        },
        {
            'question_text': 'What quality should a good driver have? (sxu96vh0)',
            'option_a': 'Driving fast',
            'option_b': 'Patience and carefulness',
            'option_c': 'Competing with others',
            'option_d': 'Loudness',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should you do if you miss an appointment due to delay? (ny5199h4)',
            'option_a': 'Give angry answers',
            'option_b': 'Make excuses',
            'option_c': 'Explain politely and apologize',
            'option_d': 'Ignore the client',
            'correct_option': 'C'
        },
        {
            'question_text': 'What should a driver check before starting a long trip? (nwp9q6h7)',
            'option_a': 'Fuel, water, oil, and tires',
            'option_b': 'Only headlights',
            'option_c': 'Seat belts only',
            'option_d': 'Radio only',
            'correct_option': 'A'
        },
        {
            'question_text': 'What should be avoided while driving on a steep slope? (lzf188ht)',
            'option_a': 'Sudden acceleration',
            'option_b': 'Sudden braking',
            'option_c': 'Continuous horn',
            'option_d': 'All of the above',
            'correct_option': 'D'
        },
        {
            'question_text': 'When parking on a hill, what should you do? (txt2xnrm)',
            'option_a': 'Leave the car in neutral',
            'option_b': 'Use handbrake and turn wheels',
            'option_c': 'Leave engine running',
            'option_d': 'Nothing special',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should a driver do when there is fog? (exo97lq1)',
            'option_a': 'Drive fast',
            'option_b': 'Use low beam lights and drive slowly',
            'option_c': 'Stop in middle of road',
            'option_d': 'Use high beam lights',
            'correct_option': 'B'
        },
    ],

    'Steel Fixer': [
        {
            'question_text': 'What is the main job of a steel fixer? (px0lizpq)',
            'option_a': 'Fixing shuttering',
            'option_b': 'Bending and fixing steel rods',
            'option_c': 'Pouring concrete',
            'option_d': 'Finishing work',
            'correct_option': 'B'
        },
        {
            'question_text': 'Rebar is made of which material? (lxg04zj9)',
            'option_a': 'Plastic',
            'option_b': 'Iron / Steel',
            'option_c': 'Aluminium',
            'option_d': 'Wood',
            'correct_option': 'B'
        },
        {
            'question_text': 'What does “millimetre bar” mean? (sxsy5868)',
            'option_a': 'Length of the bar',
            'option_b': 'Thickness (diameter) of the bar',
            'option_c': 'Weight of the bar',
            'option_d': 'Strength of the bar',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is used to bend steel bars? (kx561i58)',
            'option_a': 'Trowel',
            'option_b': 'Bending machine or manual bender',
            'option_c': 'Paint brush',
            'option_d': 'Hammer only',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is meant by "Lap Length"? (gw2m6kge)',
            'option_a': 'Extra length given to join two rods together',
            'option_b': 'Weight of the bar',
            'option_c': 'Shape of the bar',
            'option_d': 'Color of the bar',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the use of Binding Wire? (ewoli1y5)',
            'option_a': 'To tie the steel rods together',
            'option_b': 'To cut the rods',
            'option_c': 'To mix cement',
            'option_d': 'For finishing',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is used to keep steel away from the concrete surface? (tx72yy5e)',
            'option_a': 'Nail',
            'option_b': 'Cover block',
            'option_c': 'Rope',
            'option_d': 'Cement paste',
            'correct_option': 'B'
        },
        {
            'question_text': 'In which direction are rods placed in a column? (nxuh468t)',
            'option_a': 'Horizontal',
            'option_b': 'Vertical',
            'option_c': 'Diagonal',
            'option_d': 'Circular',
            'correct_option': 'B'
        },
        {
            'question_text': 'At what angle is a hook bent? (oyr04u14)',
            'option_a': '45°',
            'option_b': '90°',
            'option_c': '135°',
            'option_d': '180°',
            'correct_option': 'C'
        },
        {
            'question_text': 'What happens if steel bars are left in open air for a long time? (vxy46xhr)',
            'option_a': 'They become stronger',
            'option_b': 'They get rusted',
            'option_c': 'They become shiny',
            'option_d': 'They melt',
            'correct_option': 'B'
        },
        {
            'question_text': 'If a rod gets rusted, what should be done before reuse? (ny29l9vg)',
            'option_a': 'Wash with water',
            'option_b': 'Paint it',
            'option_c': 'Clean it with wire brush',
            'option_d': 'Leave as is',
            'correct_option': 'C'
        },
        {
            'question_text': 'What safety equipment should a steel fixer wear on site? (mx39056t)',
            'option_a': 'Cap and shirt',
            'option_b': 'Helmet, gloves, safety shoes',
            'option_c': 'Slippers',
            'option_d': 'Jacket only',
            'correct_option': 'B'
        },
        {
            'question_text': 'After fixing bars in beams and slabs, what should be checked? (sxu591fw)',
            'option_a': 'Colour of bars',
            'option_b': 'Bar spacing and cover',
            'option_c': 'Cement ratio',
            'option_d': 'Construction speed',
            'correct_option': 'B'
        },
        {
            'question_text': 'On what does the size of cover block depend? (txs6875v)',
            'option_a': 'Colour of steel',
            'option_b': 'Type of structure (slab, beam, column)',
            'option_c': 'Worker\'s choice',
            'option_d': 'Steel grade',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the use of a Chair Bar? (pxl1017o)',
            'option_a': 'To support the formwork',
            'option_b': 'To maintain the distance between top and bottom bars',
            'option_c': 'To smooth concrete',
            'option_d': 'To tie bars',
            'correct_option': 'B'
        },
        {
            'question_text': 'Why are ties used in a column? (jw36yzye)',
            'option_a': 'To hold the bars together',
            'option_b': 'To support formwork',
            'option_c': 'To make concrete shiny',
            'option_d': 'To test strength',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the purpose of a Hook? (ww562k87)',
            'option_a': 'To hold or anchor the bar strongly',
            'option_b': 'To make the bar look good',
            'option_c': 'To shorten the bar',
            'option_d': 'For finishing',
            'correct_option': 'A'
        },
        {
            'question_text': 'Why are both steel and concrete used in RCC? (swi898gj)',
            'option_a': 'Concrete is strong in compression, steel is strong in tension',
            'option_b': 'Both are light materials',
            'option_c': 'Both are waterproof',
            'option_d': 'Both are cheap',
            'correct_option': 'A'
        },
        {
            'question_text': 'What does a 10mm dia bar mean? (zxqig0gm)',
            'option_a': 'The bar is 10 inches wide',
            'option_b': 'The bar has a diameter of 10 millimetres',
            'option_c': 'The bar is 10 feet long',
            'option_d': 'The bar weighs 10 kg',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the most important thing to check at a beam–column junction? (hw5grgo3)',
            'option_a': 'Bar overlap and anchorage',
            'option_b': 'Colour of shuttering',
            'option_c': 'Cement mix ratio',
            'option_d': 'Worker safety',
            'correct_option': 'A'
        },
        {
            'question_text': 'Why is lap length more in columns? (hw8r1yl3)',
            'option_a': 'Because the load is higher',
            'option_b': 'Because the bars are shorter',
            'option_c': 'Because of design requirement',
            'option_d': 'Because it looks better',
            'correct_option': 'A'
        },
    ],

    'Warehouse Helper': [
        {
            'question_text': 'If a product\'s Batch Number is entered incorrectly, what should you do first? (xx9959sj)',
            'option_a': 'Correct it yourself',
            'option_b': 'Immediately inform the supervisor',
            'option_c': 'Tell later',
            'option_d': 'Ignore it',
            'correct_option': 'B'
        },
        {
            'question_text': 'What does "Inventory Shrinkage" mean? (lxz95j48)',
            'option_a': 'Increase in stock',
            'option_b': 'Decrease in stock due to theft or error',
            'option_c': 'New stock arrival',
            'option_d': 'Daily counting',
            'correct_option': 'B'
        },
        {
            'question_text': 'If goods on a pallet are unevenly placed, what is the risk? (nxr7r146)',
            'option_a': 'Nothing happens',
            'option_b': 'Goods may fall or get damaged',
            'option_c': 'Cleaning becomes difficult',
            'option_d': 'Weight increases',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the purpose of a Cycle Count in a warehouse? (lxnzkth2)',
            'option_a': 'Daily cleaning',
            'option_b': 'Checking record accuracy',
            'option_c': 'Training new employees',
            'option_d': 'Weekly meetings',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the most important safety rule for Dangerous Goods (DG)? (lx5827ev)',
            'option_a': 'Store with normal goods',
            'option_b': 'Use proper Warning Labels',
            'option_c': 'Store without labels',
            'option_d': 'Keep in open area',
            'correct_option': 'B'
        },
        {
            'question_text': 'If a Barcode does not scan, what should you do? (oxv0e090)',
            'option_a': 'Force scan repeatedly',
            'option_b': 'Enter the number manually and report it',
            'option_c': 'Throw away the product',
            'option_d': 'Cover it with tape',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the benefit of a Warehouse Management System (WMS)? (sx7grx81)',
            'option_a': 'Reduces workers',
            'option_b': 'Keeps automatic stock records',
            'option_c': 'Makes cleaning easier',
            'option_d': 'Prevents theft',
            'correct_option': 'B'
        },
        {
            'question_text': 'If a forklift operator places goods in the wrong place, what should the helper do? (pxout949)',
            'option_a': 'Stay silent',
            'option_b': 'Inform the supervisor and show the correct location',
            'option_c': 'Move goods by himself',
            'option_d': 'Ignore completely',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should be specially checked while working in a Cold Storage warehouse? (gxxq1m4t)',
            'option_a': 'Sound',
            'option_b': 'Body temperature and use of PPE',
            'option_c': 'Color',
            'option_d': 'Clock time',
            'correct_option': 'B'
        },
        {
            'question_text': 'If a shipment is delayed, what should a warehouse helper do? (hx58229g)',
            'option_a': 'Contact the customer directly',
            'option_b': 'Inform the supervisor and keep goods ready',
            'option_c': 'Make a new order',
            'option_d': 'Take rest',
            'correct_option': 'B'
        },
        {
            'question_text': 'When organizing warehouse materials, what should be checked first? (iywfmktq)',
            'option_a': 'Color',
            'option_b': 'Weight',
            'option_c': 'Category',
            'option_d': 'Size',
            'correct_option': 'C'
        },
        {
            'question_text': 'What does “FIFO” mean in warehousing? (wx7w9l74)',
            'option_a': 'Fast In Fast Out',
            'option_b': 'First In First Out',
            'option_c': 'First In Fast Out',
            'option_d': 'Full In Full Out',
            'correct_option': 'B'
        },
        {
            'question_text': 'Before lifting a heavy load, what must be done? (oxliv869)',
            'option_a': 'Lift quickly',
            'option_b': 'Check the weight',
            'option_c': 'Stand bent',
            'option_d': 'Skip warming up',
            'correct_option': 'B'
        },
        {
            'question_text': 'What does Inventory mean? (px2mz225)',
            'option_a': 'Purchased items',
            'option_b': 'Recorded and counted goods',
            'option_c': 'Packed goods',
            'option_d': 'Finished goods',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is a Pallet Jack used for? (oxgum8f1)',
            'option_a': 'Cleaning',
            'option_b': 'Moving goods',
            'option_c': 'Accounting',
            'option_d': 'Packaging',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the purpose of a Safety Helmet? (fysg9nyi)',
            'option_a': 'For decoration',
            'option_b': 'To protect from cold',
            'option_c': 'To protect from head injury',
            'option_d': 'To look professional',
            'correct_option': 'C'
        },
        {
            'question_text': 'Where should a Fire Extinguisher be placed in a warehouse? (qxm10ej1)',
            'option_a': 'On the main door',
            'option_b': 'At visible and accessible points',
            'option_c': 'In the office',
            'option_d': 'In storage room',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the purpose of barcoding goods in a warehouse? (nxsi40j0)',
            'option_a': 'To make them look nice',
            'option_b': 'For easy tracking and record keeping',
            'option_c': 'For decoration',
            'option_d': 'For fun',
            'correct_option': 'B'
        },
        {
            'question_text': 'How can inventory loss be prevented? (ox51v248)',
            'option_a': 'Hide goods',
            'option_b': 'Conduct regular checking',
            'option_c': 'Delete records',
            'option_d': 'Sell everything',
            'correct_option': 'B'
        },
        {
            'question_text': 'Why is ventilation important in a warehouse? (iws7409x)',
            'option_a': 'To control temperature and airflow',
            'option_b': 'For better light',
            'option_c': 'To brighten the room',
            'option_d': 'To save electricity',
            'correct_option': 'A'
        },
        {
            'question_text': 'What are Fragile Items? (qx8t26rn)',
            'option_a': 'Outdoor goods',
            'option_b': 'Easily breakable goods',
            'option_c': 'Metal items',
            'option_d': 'Plastic items',
            'correct_option': 'B'
        },
        {
            'question_text': 'During Loading and Unloading, what is most important? (ex77701k)',
            'option_a': 'Finish quickly',
            'option_b': 'Follow safety rules',
            'option_c': 'Play music',
            'option_d': 'Take photos',
            'correct_option': 'B'
        },
        {
            'question_text': 'Why is Shelf Labeling done? (lxqk30nl)',
            'option_a': 'For beauty',
            'option_b': 'For easy identification',
            'option_c': 'To increase shelf size',
            'option_d': 'For fun',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is Dead Stock in a warehouse? (zxf5ig1e)',
            'option_a': 'Broken items',
            'option_b': 'Unsold or unused items',
            'option_c': 'New stock',
            'option_d': 'Returned items',
            'correct_option': 'B'
        },
        {
            'question_text': 'If you see something placed in the wrong location, what should you do? (ix4km09i)',
            'option_a': 'Ignore it',
            'option_b': 'Inform the supervisor',
            'option_c': 'Move it secretly',
            'option_d': 'Report to police',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is a Temperature-Controlled Warehouse used for? (zwky6p05)',
            'option_a': 'Storing medicines or cold products',
            'option_b': 'Clothes',
            'option_c': 'Furniture',
            'option_d': 'Normal items',
            'correct_option': 'A'
        },
        {
            'question_text': 'What does PPE stand for? (xwgkj0yi)',
            'option_a': 'Personal Protective Equipment',
            'option_b': 'Personal Power Energy',
            'option_c': 'Public Protection Equipment',
            'option_d': 'Professional Package Equipment',
            'correct_option': 'A'
        },
        {
            'question_text': 'Before operating a Forklift, what is most important? (vx751ho6)',
            'option_a': 'Drive fast',
            'option_b': 'Wear seatbelt and safety gear',
            'option_c': 'Talk on the phone',
            'option_d': 'Avoid inspection',
            'correct_option': 'B'
        },
        {
            'question_text': 'Where should waste materials be thrown in a warehouse? (hx9gz591)',
            'option_a': 'Anywhere',
            'option_b': 'In a specific waste bin',
            'option_c': 'On the road',
            'option_d': 'With products',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the work of the Dispatch Section? (vx9ml2xq)',
            'option_a': 'Receiving goods',
            'option_b': 'Sending goods to customers',
            'option_c': 'Cleaning area',
            'option_d': 'Hiring staff',
            'correct_option': 'B'
        },
        {
            'question_text': 'How often is Stock Reconciliation done? (zx3j83ig)',
            'option_a': 'Every 6 months or yearly',
            'option_b': 'Daily',
            'option_c': 'Weekly',
            'option_d': 'When needed',
            'correct_option': 'A'
        },
        {
            'question_text': 'If water leaks inside the warehouse, what should you do? (fx4x7f90)',
            'option_a': 'Ignore it',
            'option_b': 'Inform immediately',
            'option_c': 'Move goods yourself',
            'option_d': 'Mop only',
            'correct_option': 'B'
        },
        {
            'question_text': 'What does a Hazard Sign mean? (vwg74sy9)',
            'option_a': 'Danger warning sign',
            'option_b': 'Cleaning sign',
            'option_c': 'Order sign',
            'option_d': 'Route sign',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is a Picking List? (jxpx85w7)',
            'option_a': 'Cleaning schedule',
            'option_b': 'List of items to be picked',
            'option_c': 'List of food items',
            'option_d': 'Worker schedule',
            'correct_option': 'B'
        },
        {
            'question_text': 'If goods are missing or damaged, what is your first step? (wxl8379x)',
            'option_a': 'Hide it',
            'option_b': 'Report it',
            'option_c': 'Buy new stock',
            'option_d': 'Panic',
            'correct_option': 'B'
        },
    ],

    'Mason': [
        {
            'question_text': 'What is the first step when building a brick wall? (hwjy9993)',
            'option_a': 'Set the line and level',
            'option_b': 'Apply paint',
            'option_c': 'Do water curing',
            'option_d': 'Finishing',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is used to prevent cracks between brick and block work joints? (tw3gee0w)',
            'option_a': 'Chicken mesh',
            'option_b': 'Steel rod',
            'option_c': 'Paint',
            'option_d': 'Rope',
            'correct_option': 'A'
        },
        {
            'question_text': 'Which tool is used to check the level of a wall? (lw3er5qo)',
            'option_a': 'Spirit level',
            'option_b': 'Hammer',
            'option_c': 'Trowel',
            'option_d': 'Pliers',
            'correct_option': 'A'
        },
        {
            'question_text': 'What does a 1:6 mortar mix mean? (ow84y1p8)',
            'option_a': '1 part cement, 6 parts sand',
            'option_b': '6 parts cement, 1 part sand',
            'option_c': '1 part sand, 6 parts water',
            'option_d': '1 part lime, 6 parts cement',
            'correct_option': 'A'
        },
        {
            'question_text': 'What should be checked after every course (line) of bricks? (owl1yrs0)',
            'option_a': 'Level and plumb (vertical alignment)',
            'option_b': 'Colour of bricks',
            'option_c': 'Smell of mortar',
            'option_d': 'Size of sand',
            'correct_option': 'A'
        },
        {
            'question_text': 'When laying bricks, which side should the "frog" face? (txe7i612)',
            'option_a': 'Upward',
            'option_b': 'Downward',
            'option_c': 'Sideways',
            'option_d': 'In the middle',
            'correct_option': 'B'
        },
        {
            'question_text': 'Which tool is used to make the plaster surface smooth? (iwlfxxo1)',
            'option_a': 'Steel trowel',
            'option_b': 'Brush',
            'option_c': 'Hammer',
            'option_d': 'Sandpaper',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the usual thickness of plaster? (pw7ypru7)',
            'option_a': '12 mm',
            'option_b': '5 mm',
            'option_c': '20 mm',
            'option_d': '40 mm',
            'correct_option': 'A'
        },
        {
            'question_text': 'Before plastering the ceiling, what is applied to the RCC surface? (lw0h0500)',
            'option_a': 'Cement slurry',
            'option_b': 'Paint',
            'option_c': 'Lime wash',
            'option_d': 'Water only',
            'correct_option': 'A'
        },
        {
            'question_text': 'What can be added to plaster to make it waterproof? (rwqz75x2)',
            'option_a': 'Liquid compound',
            'option_b': 'Extra water',
            'option_c': 'Dry sand',
            'option_d': 'Lime',
            'correct_option': 'A'
        },
        {
            'question_text': 'What happens if vertical joints in a block wall are placed in one line? (fwg656ol)',
            'option_a': 'Cracks appear in the wall',
            'option_b': 'Finishing becomes poor',
            'option_c': 'Work speed reduces',
            'option_d': 'Strength increases',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the purpose of making screed points on a wall? (iwl44u4u)',
            'option_a': 'To set the plaster level',
            'option_b': 'For decoration',
            'option_c': 'For painting',
            'option_d': 'For foundation',
            'correct_option': 'A'
        },
        {
            'question_text': 'At what level is the DPC (Damp Proof Course) provided? (kw4krslo)',
            'option_a': 'Just above ground level',
            'option_b': 'Under the roof',
            'option_c': 'Below the foundation',
            'option_d': 'In the ceiling',
            'correct_option': 'A'
        },
        {
            'question_text': 'After masonry work, for how many days should curing be done at minimum? (jw3z580k)',
            'option_a': '7 days',
            'option_b': '2 days',
            'option_c': '1 day',
            'option_d': '14 days',
            'correct_option': 'A'
        },
        {
            'question_text': 'What should be checked most carefully while making wall corners? (kw645265)',
            'option_a': 'Plumb (vertical) and alignment',
            'option_b': 'Colour matching',
            'option_c': 'Paint quality',
            'option_d': 'Number of bricks',
            'correct_option': 'A'
        },
        {
            'question_text': 'With one bag of cement, how much plaster area can be covered in 1:4 mortar (12 mm thick)? (kwuf21s3)',
            'option_a': 'Around 10 sq.m',
            'option_b': '2 sq.m',
            'option_c': '25 sq.m',
            'option_d': '6 sq.m',
            'correct_option': 'A'
        },
        {
            'question_text': 'Why do cracks appear in ceiling plaster? (lw8lz7m3)',
            'option_a': 'Due to quick drying or excess water',
            'option_b': 'Because paint is not applied',
            'option_c': 'Due to soft sand',
            'option_d': 'Bad mixing',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the normal height of one course (layer) of bricks including mortar? (wwlj99ol)',
            'option_a': '75 mm',
            'option_b': '100 mm',
            'option_c': '125 mm',
            'option_d': '150 mm',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the first step before starting plastering on a wall? (vw58w292)',
            'option_a': 'Clean the surface and wet it with water',
            'option_b': 'Apply paint',
            'option_c': 'Keep cement dry',
            'option_d': 'Apply primer',
            'correct_option': 'A'
        },
        {
            'question_text': 'What safety equipment should a mason wear on site? (vw380m0y)',
            'option_a': 'Helmet, gloves, and safety shoes',
            'option_b': 'Cap and slippers',
            'option_c': 'Shirt and jeans',
            'option_d': 'Belt only',
            'correct_option': 'A'
        },
    ],

    "Dozer Operator": [
        {
            "question_text": "What is the main function of a bulldozer? (exxtqxhe)",
            "option_a": "Lifting materials",
            "option_b": "Pushing and leveling soil",
            "option_c": "Mixing concrete",
            "option_d": "Drilling holes",
            "correct_option": "B"
        },
        {
            "question_text": "What safety gear should a dozer operator wear? (fw6vxrz5)",
            "option_a": "Helmet and boots",
            "option_b": "T-shirt only",
            "option_c": "Formal shoes",
            "option_d": "No gear",
            "correct_option": "A"
        },
        {
            "question_text": "How often should hydraulic oil be checked? (yw058wp9)",
            "option_a": "Daily",
            "option_b": "Weekly",
            "option_c": "Monthly",
            "option_d": "Yearly",
            "correct_option": "A"
        },
        {
            "question_text": "What should be done before starting the dozer? (1wsvp15x)",
            "option_a": "Check fluids and surroundings",
            "option_b": "Start immediately",
            "option_c": "Ignore inspection",
            "option_d": "Call supervisor first",
            "correct_option": "A"
        },
        {
            "question_text": "Which attachment is used for fine grading? (1xfzh02x)",
            "option_a": "Ripper",
            "option_b": "Blade",
            "option_c": "Bucket",
            "option_d": "Drum",
            "correct_option": "B"
        },
        {
            "question_text": "When working on slopes, how should the dozer move? (3x5q3ipv)",
            "option_a": "Perpendicular to slope",
            "option_b": "Along slope direction",
            "option_c": "Randomly",
            "option_d": "Fast speed",
            "correct_option": "B"
        },
        {
            "question_text": "Why is track tension important? (nx333r7z)",
            "option_a": "Improves visibility",
            "option_b": "Prevents track wear and slippage",
            "option_c": "Increases engine power",
            "option_d": "Reduces operator fatigue",
            "correct_option": "B"
        },
        {
            "question_text": "What should be avoided when reversing? (yxqug43n)",
            "option_a": "Checking mirrors",
            "option_b": "Blind backing",
            "option_c": "Using alarms",
            "option_d": "Using a guide",
            "correct_option": "B"
        },
        {
            "question_text": "Which part controls the dozer blade? (7wijus5s)",
            "option_a": "Joystick or lever",
            "option_b": "Gear stick",
            "option_c": "Pedal",
            "option_d": "Steering wheel",
            "correct_option": "A"
        },
        {
            "question_text": "When should pre-start inspection be done? (6x4k9sfi)",
            "option_a": "After lunch",
            "option_b": "Before every shift",
            "option_c": "At month end",
            "option_d": "Never",
            "correct_option": "B"
        },
        {
            "question_text": "What is the ripper used for? (7wwi3yzz)",
            "option_a": "Breaking hard soil or rock",
            "option_b": "Pushing loose dirt",
            "option_c": "Lifting objects",
            "option_d": "Towing vehicles",
            "correct_option": "A"
        },
        {
            "question_text": "Which area is considered a blind spot? (twxi1x59)",
            "option_a": "Behind the dozer",
            "option_b": "In front of blade",
            "option_c": "Under seat",
            "option_d": "None",
            "correct_option": "A"
        },
        {
            "question_text": "What should be done in case of hydraulic leak? (xx55y4zp)",
            "option_a": "Ignore it",
            "option_b": "Report and shut down",
            "option_c": "Continue work",
            "option_d": "Cover with tape",
            "correct_option": "B"
        },
        {
            "question_text": "How should a dozer be parked? (4xkwmwhu)",
            "option_a": "On slope",
            "option_b": "Level ground with brake engaged",
            "option_c": "With engine running",
            "option_d": "Next to pit edge",
            "correct_option": "B"
        },
        {
            "question_text": "What fuel does a dozer typically use? (7weujuv3)",
            "option_a": "Diesel",
            "option_b": "Petrol",
            "option_c": "Gas",
            "option_d": "Electric",
            "correct_option": "A"
        }
    ],
    "Loader Operator": [
        {
            "question_text": "What is the primary purpose of a wheel loader? (rxv95e7k)",
            "option_a": "Digging trenches",
            "option_b": "Loading materials",
            "option_c": "Drilling holes",
            "option_d": "Transporting passengers",
            "correct_option": "B"
        },
        {
            "question_text": "How often should tire pressure be checked? (iwmtefue)",
            "option_a": "Daily",
            "option_b": "Weekly",
            "option_c": "Monthly",
            "option_d": "Never",
            "correct_option": "A"
        },
        {
            "question_text": "What should be done before lifting a full bucket? (exukelk7)",
            "option_a": "Over-rev engine",
            "option_b": "Ensure balance and clearance",
            "option_c": "Turn sharply",
            "option_d": "Ignore weight limits",
            "correct_option": "B"
        },
        {
            "question_text": "What type of bucket is used for loose materials? (0x95ggps)",
            "option_a": "Rock bucket",
            "option_b": "Light material bucket",
            "option_c": "Heavy-duty bucket",
            "option_d": "Trench bucket",
            "correct_option": "B"
        },
        {
            "question_text": "When reversing, what should the operator do? (9wl5n5p5)",
            "option_a": "Use mirrors and alarms",
            "option_b": "Speed up",
            "option_c": "Turn off alarm",
            "option_d": "Look forward only",
            "correct_option": "A"
        },
        {
            "question_text": "What fluid is essential for hydraulic systems? (nx4pj7hy)",
            "option_a": "Water",
            "option_b": "Hydraulic oil",
            "option_c": "Coolant",
            "option_d": "Brake fluid",
            "correct_option": "B"
        },
        {
            "question_text": "Which component lifts the bucket? (zwklkq0v)",
            "option_a": "Hydraulic cylinders",
            "option_b": "Engine block",
            "option_c": "Axle",
            "option_d": "Pump motor",
            "correct_option": "A"
        },
        {
            "question_text": "How can fuel efficiency be improved? (hxfmww5h)",
            "option_a": "Overloading",
            "option_b": "Smooth operation and maintenance",
            "option_c": "High-speed driving",
            "option_d": "Constant idling",
            "correct_option": "B"
        },
        {
            "question_text": "What must be done after refueling? (ewmq9h2h)",
            "option_a": "Check for leaks",
            "option_b": "Start without inspection",
            "option_c": "Leave cap open",
            "option_d": "Drive fast",
            "correct_option": "A"
        },
        {
            "question_text": "What safety step is needed before maintenance? (kwq9hwog)",
            "option_a": "Lockout/tagout",
            "option_b": "Engine on",
            "option_c": "Tilt bucket high",
            "option_d": "No need",
            "correct_option": "A"
        },
        {
            "question_text": "What indicates low hydraulic pressure? (7xumpm55)",
            "option_a": "Normal operation",
            "option_b": "Slow bucket response",
            "option_c": "Fast lifting",
            "option_d": "No change",
            "correct_option": "B"
        },
        {
            "question_text": "Which system controls movement? (sw39ot9p)",
            "option_a": "Transmission",
            "option_b": "Fuel line",
            "option_c": "Cooling",
            "option_d": "Lighting",
            "correct_option": "A"
        },
        {
            "question_text": "What should be avoided when traveling with load? (gwj90r35)",
            "option_a": "High speed turns",
            "option_b": "Slow lifting",
            "option_c": "Checking mirrors",
            "option_d": "Low gear use",
            "correct_option": "A"
        },
        {
            "question_text": "When operating near people, what should be used? (2wrk56xj)",
            "option_a": "Warning signals",
            "option_b": "Silent mode",
            "option_c": "Fast gear",
            "option_d": "Engine brake",
            "correct_option": "A"
        },
        {
            "question_text": "What is bucket rollback used for? (1wsh2mwo)",
            "option_a": "To hold material securely",
            "option_b": "To dump faster",
            "option_c": "To dig deep",
            "option_d": "To steer",
            "correct_option": "A"
        }
    ],
    "Trala Driver": [
        {
            "question_text": "What is a trala used for? (vxkzlk3o)",
            "option_a": "Passenger transport",
            "option_b": "Transport heavy goods",
            "option_c": "Carrying tools",
            "option_d": "Small packages",
            "correct_option": "B"
        },
        {
            "question_text": "What is essential before loading? (vwfqksfx)",
            "option_a": "Load balance and straps",
            "option_b": "Colour check",
            "option_c": "Radio tune",
            "option_d": "Clean tires",
            "correct_option": "A"
        },
        {
            "question_text": "What speed must tralas maintain on highways? (hx3u5tp6)",
            "option_a": "Normal car speed",
            "option_b": "Reduced based on load",
            "option_c": "Max 100km/h",
            "option_d": "No limit",
            "correct_option": "B"
        },
        {
            "question_text": "What to check in braking system? (zxv7h867)",
            "option_a": "Only pedal",
            "option_b": "Air pressure and lines",
            "option_c": "Paint",
            "option_d": "Seat",
            "correct_option": "B"
        },
        {
            "question_text": "What document is needed for oversized loads? (iwemf508)",
            "option_a": "Permit",
            "option_b": "Map",
            "option_c": "None",
            "option_d": "License",
            "correct_option": "A"
        },
        {
            "question_text": "What indicates overload? (4xos3gl4)",
            "option_a": "Smooth drive",
            "option_b": "Tyre bulge",
            "option_c": "Normal braking",
            "option_d": "Light steering",
            "correct_option": "B"
        },
        {
            "question_text": "How to prevent load shifting? (qwom723l)",
            "option_a": "Chains and straps",
            "option_b": "Rope",
            "option_c": "Ignore",
            "option_d": "Wooden blocks only",
            "correct_option": "A"
        },
        {
            "question_text": "When should inspection be done? (hxovqrj6)",
            "option_a": "After loading",
            "option_b": "Before and after journey",
            "option_c": "Only before",
            "option_d": "Never",
            "correct_option": "B"
        },
        {
            "question_text": "How to ensure road safety? (0w6o5zeg)",
            "option_a": "Proper lights and markings",
            "option_b": "Loud horn",
            "option_c": "Speeding",
            "option_d": "Wide turns",
            "correct_option": "A"
        },
        {
            "question_text": "What is essential at night? (lwrm3h5x)",
            "option_a": "Lights and reflectors",
            "option_b": "Music",
            "option_c": "Fog",
            "option_d": "Windows open",
            "correct_option": "A"
        },
        {
            "question_text": "What to do before reversing? (9w3u3r2x)",
            "option_a": "Check mirrors and horns",
            "option_b": "Speed up",
            "option_c": "Ignore",
            "option_d": "Call police",
            "correct_option": "A"
        },
        {
            "question_text": "What causes jackknifing? (qw2l5i1r)",
            "option_a": "Improper braking",
            "option_b": "Proper speed",
            "option_c": "Good road",
            "option_d": "Light load",
            "correct_option": "A"
        },
        {
            "question_text": "Which license is required? (jwpxtixi)",
            "option_a": "HTV",
            "option_b": "Car",
            "option_c": "Bike",
            "option_d": "LTV",
            "correct_option": "A"
        },
        {
            "question_text": "When should brakes be checked? (3w2q3mp2)",
            "option_a": "Daily",
            "option_b": "Monthly",
            "option_c": "After 10000km",
            "option_d": "Never",
            "correct_option": "A"
        },
        {
            "question_text": "Why use safety cones? (rwulw0l2)",
            "option_a": "Mark parked trala",
            "option_b": "Decoration",
            "option_c": "Speed control",
            "option_d": "Measure distance",
            "correct_option": "A"
        }
    ],
    "Grader Operator": [
        {
            "question_text": "What is grader used for? (lx2970iu)",
            "option_a": "Lifting",
            "option_b": "Leveling surfaces",
            "option_c": "Mixing",
            "option_d": "Pushing loads",
            "correct_option": "B"
        },
        {
            "question_text": "Best blade angle? (rxhi29lk)",
            "option_a": "90°",
            "option_b": "30-45°",
            "option_c": "0°",
            "option_d": "60°",
            "correct_option": "B"
        },
        {
            "question_text": "How to operate on slope? (rx883fpe)",
            "option_a": "Fast",
            "option_b": "Controlled speed",
            "option_c": "Reverse only",
            "option_d": "Full blade",
            "correct_option": "B"
        },
        {
            "question_text": "Main safety near traffic? (ww8vlzyk)",
            "option_a": "Warning signs",
            "option_b": "Ignore",
            "option_c": "Speed",
            "option_d": "No signal",
            "correct_option": "A"
        },
        {
            "question_text": "Before operation check? (rwm50820)",
            "option_a": "Hydraulics, blade, tires",
            "option_b": "Fuel only",
            "option_c": "Music",
            "option_d": "Color",
            "correct_option": "A"
        },
        {
            "question_text": "Which control lifts blade? (kwtxmr7s)",
            "option_a": "Joystick",
            "option_b": "Pedal",
            "option_c": "Gear",
            "option_d": "Horn",
            "correct_option": "A"
        },
        {
            "question_text": "What is scarifier used for? (3wwgh55i)",
            "option_a": "Loosen compact soil",
            "option_b": "Level surface",
            "option_c": "Polish blade",
            "option_d": "Lubricate",
            "correct_option": "A"
        },
        {
            "question_text": "When to inspect blade? (lwjupfpy)",
            "option_a": "Before use",
            "option_b": "After work",
            "option_c": "Never",
            "option_d": "Yearly",
            "correct_option": "A"
        },
        {
            "question_text": "Best practice in wet soil? (ww5egvh0)",
            "option_a": "Slow and steady",
            "option_b": "Full throttle",
            "option_c": "Reverse",
            "option_d": "Idle",
            "correct_option": "A"
        },
        {
            "question_text": "How to maintain grade? (4wu459vf)",
            "option_a": "Consistent speed and depth",
            "option_b": "High speed",
            "option_c": "Uneven turns",
            "option_d": "Stop often",
            "correct_option": "A"
        },
        {
            "question_text": "Safety when crossing road? (zwzo8jog)",
            "option_a": "Use flagman",
            "option_b": "Drive fast",
            "option_c": "No lights",
            "option_d": "Ignore",
            "correct_option": "A"
        },
        {
            "question_text": "How to handle sharp turns? (vwwgzknm)",
            "option_a": "Reduce speed",
            "option_b": "Accelerate",
            "option_c": "Brake hard",
            "option_d": "Lift blade high",
            "correct_option": "A"
        },
        {
            "question_text": "Why use blade pitch? (mw5m11fq)",
            "option_a": "Adjust cut depth",
            "option_b": "Increase speed",
            "option_c": "Reduce load",
            "option_d": "Change tire angle",
            "correct_option": "A"
        },
        {
            "question_text": "What to do if visibility poor? (hw3wvkfm)",
            "option_a": "Use lights and signals",
            "option_b": "Continue",
            "option_c": "Speed up",
            "option_d": "Ignore",
            "correct_option": "A"
        },
        {
            "question_text": "Where to park? (4w39rese)",
            "option_a": "Flat safe ground",
            "option_b": "Slope",
            "option_c": "Hilltop",
            "option_d": "On road",
            "correct_option": "A"
        }
    ],
    'Project Engineer': [
        {
            'question_text': 'Why is a baseline schedule essential in project management? (kxx5n1t7)',
            'option_a': 'It records equipment serial numbers',
            'option_b': 'It tracks approved time and cost targets',
            'option_c': 'It measures worker attendance',
            'option_d': 'It replaces procurement logs',
            'correct_option': 'B'
        },
        {
            'question_text': 'What does an earned value analysis compare? (myx7r2p5)',
            'option_a': 'Design ideas versus vendor lists',
            'option_b': 'Fuel usage with payroll',
            'option_c': 'Work performed, planned value, and actual cost',
            'option_d': 'Safety records to weather data',
            'correct_option': 'C'
        },
        {
            'question_text': 'Why must change orders be documented formally? (pxx3m8t4)',
            'option_a': 'To track lunch expenses',
            'option_b': 'To capture scope, time, and budget impacts accurately',
            'option_c': 'To update company logos',
            'option_d': 'To avoid team meetings',
            'correct_option': 'B'
        },
        {
            'question_text': 'Which tool helps identify task dependencies? (swx9t5k6)',
            'option_a': 'Gantt chart',
            'option_b': 'Lunch roster',
            'option_c': 'Safety checklist',
            'option_d': 'Payroll sheet',
            'correct_option': 'A'
        },
        {
            'question_text': 'Why is a risk register maintained? (nxx2p4q7)',
            'option_a': 'To schedule vacations',
            'option_b': 'To record potential issues with mitigation actions',
            'option_c': 'To store supplier invoices',
            'option_d': 'To list crew members',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the main purpose of a kickoff meeting? (gwx6n3p8)',
            'option_a': 'To align stakeholders on objectives and deliverables',
            'option_b': 'To assign parking spots',
            'option_c': 'To sign paychecks',
            'option_d': 'To plan company outings',
            'correct_option': 'A'
        },
        {
            'question_text': 'Why should procurement lead times be tracked? (hxy4t2k1)',
            'option_a': 'To adjust staff uniforms',
            'option_b': 'To prevent schedule delays from late materials',
            'option_c': 'To reduce contractor meetings',
            'option_d': 'To predict weather',
            'correct_option': 'B'
        },
        {
            'question_text': 'Which document captures lessons learned for future projects? (uxy7m6p3)',
            'option_a': 'Daily toolbox talk',
            'option_b': 'Project closeout report',
            'option_c': 'Expense voucher',
            'option_d': 'Asset register',
            'correct_option': 'B'
        },
        {
            'question_text': 'Why is stakeholder communication planning critical? (kxy1r5t8)',
            'option_a': 'To set the lunch menu',
            'option_b': 'To ensure the right information reaches the right audience on time',
            'option_c': 'To determine overtime rates',
            'option_d': 'To reduce drawing revisions',
            'correct_option': 'B'
        },
        {
            'question_text': 'Which metric shows how efficiently resources are used? (mwx5n4q2)',
            'option_a': 'Cost performance index',
            'option_b': 'Weather variance index',
            'option_c': 'Design creativity score',
            'option_d': 'Inventory turnover ratio',
            'correct_option': 'A'
        },
        {
            'question_text': 'Why must site instructions be logged promptly? (pyx8t1m6)',
            'option_a': 'To update company branding',
            'option_b': 'To arrange staff meals',
            'option_c': 'To track contractual directives and cost implications',
            'option_d': 'To store material samples',
            'correct_option': 'C'
        },
        {
            'question_text': 'How does a project engineer monitor subcontractor performance? (sxx2r9k7)',
            'option_a': 'By random guesses',
            'option_b': 'By comparing progress and quality against contracts',
            'option_c': 'By reviewing lunch orders',
            'option_d': 'By changing drawings often',
            'correct_option': 'B'
        },
        {
            'question_text': 'Why are weekly progress reports prepared? (nwx7p3q5)',
            'option_a': 'To remind staff of birthdays',
            'option_b': 'To document status, issues, and next steps for stakeholders',
            'option_c': 'To adjust payroll',
            'option_d': 'To order stationery',
            'correct_option': 'B'
        },
        {
            'question_text': 'Which process ensures completed work meets specifications? (gwx9m2p4)',
            'option_a': 'Quality assurance and inspections',
            'option_b': 'Canteen management',
            'option_c': 'Team building events',
            'option_d': 'Holiday scheduling',
            'correct_option': 'A'
        },
        {
            'question_text': 'Why must project engineers update cash flow forecasts? (hxy6t4k3)',
            'option_a': 'To set office music playlists',
            'option_b': 'To ensure funding needs are anticipated and controlled',
            'option_c': 'To manage parking allocations',
            'option_d': 'To hire new drivers',
            'correct_option': 'B'
        }
    ],
    'Translation Operations Officer': [
        {
            'question_text': 'What is the main duty of a Translation Operations Officer? (kx7g5m9u)',
            'option_a': 'Translating documents',
            'option_b': 'Managing client bookings and translator coordination',
            'option_c': 'Printing certificates',
            'option_d': 'Making advertisements',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should the officer do after a client books a translation service? (lx9x3t7q)',
            'option_a': 'Ignore the booking',
            'option_b': 'Make a follow-up call to confirm details',
            'option_c': 'Wait for the client to call again',
            'option_d': 'Cancel the booking',
            'correct_option': 'B'
        },
        {
            'question_text': 'If a client has a problem with the booking, the officer should: (mx1x6p8r)',
            'option_a': 'End the call',
            'option_b': 'Report and resolve the issue professionally',
            'option_c': 'Avoid contact',
            'option_d': 'Delete the record',
            'correct_option': 'B'
        },
        {
            'question_text': 'Who arranges the translator appointment? (px5x8n6y)',
            'option_a': 'Client',
            'option_b': 'Operational Officer',
            'option_c': 'Accountant',
            'option_d': 'Receptionist',
            'correct_option': 'B'
        },
        {
            'question_text': 'What are the common modes of translation appointments? (hw4m7t9k)',
            'option_a': 'Face-to-face, by call, or document-based',
            'option_b': 'Video editing',
            'option_c': 'Social media',
            'option_d': 'Classroom sessions',
            'correct_option': 'A'
        },
        {
            'question_text': 'If a translator is not available for a confirmed booking, what should be done? (nx6x5q8t)',
            'option_a': 'Cancel the job immediately',
            'option_b': 'Arrange another translator and inform the client',
            'option_c': 'Delay for a week',
            'option_d': 'Ignore the client',
            'correct_option': 'B'
        },
        {
            'question_text': 'Which skill is most important for this role? (kw8w3s7p)',
            'option_a': 'Strong communication and coordination',
            'option_b': 'Graphic design',
            'option_c': 'Typing speed',
            'option_d': 'Cooking',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the first step before confirming a translator? (pw2w6m9r)',
            'option_a': 'Checking translator\'s availability and specialty',
            'option_b': 'Asking client to wait',
            'option_c': 'Sending invoice first',
            'option_d': 'Assigning anyone randomly',
            'correct_option': 'A'
        },
        {
            'question_text': 'What should be recorded after every follow-up call? (mz5w9q3u)',
            'option_a': 'Nothing',
            'option_b': 'Weather update',
            'option_c': 'Translator\'s lunch break',
            'option_d': 'Client feedback and confirmation status',
            'correct_option': 'D'
        },
        {
            'question_text': 'How does an officer confirm a booking with the client? (nw7w1t6q)',
            'option_a': 'Through phone call or email confirmation',
            'option_b': 'By letter',
            'option_c': 'By social media comment',
            'option_d': 'By waiting silently',
            'correct_option': 'A'
        },
        {
            'question_text': 'What should be done if the client requests a different appointment type (e.g., face-to-face instead of call)? (qx3x8p5n)',
            'option_a': 'Decline immediately',
            'option_b': 'Adjust the booking and confirm new details',
            'option_c': 'Charge extra without informing',
            'option_d': 'Ignore the change',
            'correct_option': 'B'
        },
        {
            'question_text': 'What document is important to check before finalizing translation? (rw1w5m7k)',
            'option_a': 'Client\'s ID and original papers',
            'option_b': 'Translator\'s favorite color',
            'option_c': 'Company logo',
            'option_d': 'Marketing brochure',
            'correct_option': 'A'
        },
        {
            'question_text': 'If the translator reports a client issue, what should the officer do? (sw4w8t6p)',
            'option_a': 'Resolve it quickly and professionally',
            'option_b': 'Blame the client',
            'option_c': 'Leave it unsolved',
            'option_d': 'Hide it',
            'correct_option': 'A'
        },
        {
            'question_text': 'Why are follow-up calls important? (tz6w2q9m)',
            'option_a': 'To cancel appointments',
            'option_b': 'To advertise products',
            'option_c': 'To delay work',
            'option_d': 'To confirm booking accuracy and maintain client trust',
            'correct_option': 'D'
        },
        {
            'question_text': 'What is the preferred way to handle an unhappy client? (uw8w5n4r)',
            'option_a': 'Listen carefully and find a solution',
            'option_b': 'Ignore their complaint',
            'option_c': 'Transfer the call repeatedly',
            'option_d': 'End the conversation quickly',
            'correct_option': 'A'
        },
        {
            'question_text': 'Which of the following should always be updated in records? (vw3w7p8k)',
            'option_a': 'Appointment time, date, and mode',
            'option_b': 'Translator\'s favorite movie',
            'option_c': 'Random notes',
            'option_d': 'Office snacks list',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is a translator\'s "face-to-face appointment"? (wx5w1m9t)',
            'option_a': 'Translation through text message',
            'option_b': 'Meeting the client in person for translation',
            'option_c': 'Document printing',
            'option_d': 'Email exchange',
            'correct_option': 'B'
        },
        {
            'question_text': 'What does "call appointment" mean in translation service? (yw7w4q5n)',
            'option_a': 'Translation done through phone conversation',
            'option_b': 'Video advertisement',
            'option_c': 'Office interview',
            'option_d': 'Social media post',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the main goal of the operations officer? (zw2w6t8p)',
            'option_a': 'Ensure smooth communication between client and translator',
            'option_b': 'Write new articles',
            'option_c': 'Design posters',
            'option_d': 'Hire drivers',
            'correct_option': 'A'
        },
        {
            'question_text': 'What should the officer do if a client does not answer the follow-up call? (hw9w3m7q)',
            'option_a': 'Leave a polite message or send a reminder',
            'option_b': 'Mark booking as cancelled immediately',
            'option_c': 'Ignore it',
            'option_d': 'Delete the client record',
            'correct_option': 'A'
        },
        {
            'question_text': 'What must be double-checked before translation begins? (jy4w8t5n)',
            'option_a': 'Client\'s mood',
            'option_b': 'Translator\'s address only',
            'option_c': 'Date, time, language pair, and client instructions',
            'option_d': 'Random note',
            'correct_option': 'C'
        },
        {
            'question_text': 'Why is coordination between translation and operations team important? (kw6w1p7r)',
            'option_a': 'To ensure bookings are accurate and work runs smoothly',
            'option_b': 'To increase staff size',
            'option_c': 'To delay delivery',
            'option_d': 'To create confusion',
            'correct_option': 'A'
        },
        {
            'question_text': 'Which system or tool can help in managing bookings? (lw8w4q6t)',
            'option_a': 'Excel or CRM software',
            'option_b': 'Photo editor',
            'option_c': 'Music player',
            'option_d': 'Social media app',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the best way to confirm translator\'s appointment? (mz2w7n5p)',
            'option_a': 'Avoid confirmation',
            'option_b': 'Assume availability',
            'option_c': 'Wait till the last moment',
            'option_d': 'Send message and get confirmation in writing',
            'correct_option': 'D'
        },
        {
            'question_text': 'What is the final task after a successful translation appointment? (nw5w9t3k)',
            'option_a': 'Record completion, take feedback, and close the case',
            'option_b': 'Delete all records',
            'option_c': 'Start a new booking without closing the old one',
            'option_d': 'Ignore the client',
            'correct_option': 'A'
        }
    ],
    'Customer Relation Officer': [
        {
            'question_text': 'What is the main duty of a Customer Relation Officer in an immigration office? (kw7w2m8r)',
            'option_a': 'To communicate with clients and guide them about visa processes',
            'option_b': 'To stamp passports',
            'option_c': 'To take interviews of candidates',
            'option_d': 'To translate documents',
            'correct_option': 'A'
        },
        {
            'question_text': 'When a new client visits or calls, what should the CRO do first? (ly9w5t7q)',
            'option_a': 'Ignore the call',
            'option_b': 'Ask for payment immediately',
            'option_c': 'Greet politely and collect basic client information',
            'option_d': 'Transfer to another office',
            'correct_option': 'C'
        },
        {
            'question_text': 'What should the CRO check before submitting a client\'s file? (mw4w8p6n)',
            'option_a': 'All required documents are complete and verified',
            'option_b': 'Just the photo',
            'option_c': 'Only CNIC copy',
            'option_d': 'Nothing',
            'correct_option': 'A'
        },
        {
            'question_text': 'If a client asks about visa status, what is the CRO\'s responsibility? (nw6w1q9t)',
            'option_a': 'Check the system and give an updated status clearly',
            'option_b': 'Say "I don\'t know"',
            'option_c': 'Ignore the question',
            'option_d': 'Give a wrong answer',
            'correct_option': 'A'
        },
        {
            'question_text': 'Why are follow-up calls important for a CRO? (px8w3m5r)',
            'option_a': 'To waste time',
            'option_b': 'To confirm client interest and update them about progress',
            'option_c': 'To chat casually',
            'option_d': 'To close the case early',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should a CRO do if a client\'s document is missing or unclear? (qw2w6t8k)',
            'option_a': 'Inform the client immediately and request the correct one',
            'option_b': 'Keep the file pending forever',
            'option_c': 'Guess the missing part',
            'option_d': 'Submit the file anyway',
            'correct_option': 'A'
        },
        {
            'question_text': 'Which of the following is the best way to build client trust? (rw5w9p3n)',
            'option_a': 'Give correct information and regular updates',
            'option_b': 'Make false promises',
            'option_c': 'Delay responses',
            'option_d': 'Ignore feedback',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the best communication method for official client updates? (sy7w4m6t)',
            'option_a': 'SMS without name',
            'option_b': 'Social media post',
            'option_c': 'Through call, WhatsApp, or official email',
            'option_d': 'No communication',
            'correct_option': 'C'
        },
        {
            'question_text': 'When a client confirms a visa service, what should the CRO do next? (tw1w8q5r)',
            'option_a': 'Record details and forward the case to the processing department',
            'option_b': 'Wait for one week',
            'option_c': 'Forget to note it',
            'option_d': 'Cancel the booking',
            'correct_option': 'A'
        },
        {
            'question_text': 'Why must CROs maintain daily records? (uw3w2n7k)',
            'option_a': 'To track each client\'s case and report progress to management',
            'option_b': 'For decoration',
            'option_c': 'For no reason',
            'option_d': 'To delete data later',
            'correct_option': 'A'
        },
        {
            'question_text': 'How should a CRO respond if a client is angry about delay? (vz6w5t9p)',
            'option_a': 'Blame someone else',
            'option_b': 'Argue back',
            'option_c': 'Hang up',
            'option_d': 'Stay calm, explain the reason, and assure quick action',
            'correct_option': 'D'
        },
        {
            'question_text': 'What is one important quality for a CRO in immigration work? (ww8w7m4q)',
            'option_a': 'Patience and professionalism',
            'option_b': 'Rudeness',
            'option_c': 'Laziness',
            'option_d': 'Ignoring calls',
            'correct_option': 'A'
        },
        {
            'question_text': 'When a client\'s visa is approved, what is the next step? (xw2w9p6n)',
            'option_a': 'Inform the client and guide about travel or medical requirements',
            'option_b': 'Keep it secret',
            'option_c': 'Wait for client to call',
            'option_d': 'Delete the record',
            'correct_option': 'A'
        },
        {
            'question_text': 'What should a CRO never promise a client? (yx5w1q8t)',
            'option_a': 'Updates about process',
            'option_b': 'Guaranteed visa approval',
            'option_c': 'Information about documents',
            'option_d': 'Office working hours',
            'correct_option': 'B'
        },
        {
            'question_text': 'If a client asks about Gulf job requirements, the CRO should: (zw7w3m5r)',
            'option_a': 'Explain job type, salary, and documents needed clearly',
            'option_b': 'Say "We don\'t know"',
            'option_c': 'Give random answers',
            'option_d': 'Ignore the query',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the main goal of a CRO in an immigration office? (hy9w6t2p)',
            'option_a': 'Only collecting payments',
            'option_b': 'Only taking phone calls',
            'option_c': 'Client satisfaction and smooth process from start to finish',
            'option_d': 'Avoiding client follow-up',
            'correct_option': 'C'
        },
        {
            'question_text': 'Why should CROs use a client tracking sheet or CRM? (jw1w8m4q)',
            'option_a': 'To monitor status and follow-ups accurately',
            'option_b': 'To make office look busy',
            'option_c': 'To confuse staff',
            'option_d': 'To delay work',
            'correct_option': 'A'
        },
        {
            'question_text': 'What should a CRO do if a client gives false documents? (kw3w5p7n)',
            'option_a': 'Report it to the manager or compliance department immediately',
            'option_b': 'Accept quietly',
            'option_c': 'Hide it',
            'option_d': 'Approve anyway',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the correct behavior during client meetings? (lx6w9t1r)',
            'option_a': 'Rude and casual',
            'option_b': 'Professional, polite, and informative',
            'option_c': 'Silent and confused',
            'option_d': 'Overconfident and careless',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should a CRO do before ending a client call? (mw8w2q4k)',
            'option_a': 'Confirm understanding and next step clearly',
            'option_b': 'Hang up suddenly',
            'option_c': 'Ask personal questions',
            'option_d': 'Ignore closing summary',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the most common client concern in immigration services? (ny1w5m7p)',
            'option_a': 'Coffee availability',
            'option_b': 'Office color',
            'option_c': 'Visa approval time and document requirements',
            'option_d': 'Website design',
            'correct_option': 'C'
        },
        {
            'question_text': 'When should CRO update the management team? (pw3w7t9n)',
            'option_a': 'Daily or when there\'s any issue or progress in client cases',
            'option_b': 'Once a year',
            'option_c': 'Never',
            'option_d': 'Only during holidays',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is a CRO\'s role during job offer or employment letter issuance? (qw6w1p8r)',
            'option_a': 'Confirm details with client and ensure signature or acceptance',
            'option_b': 'Ignore the letter',
            'option_c': 'Print and throw away',
            'option_d': 'Do nothing',
            'correct_option': 'A'
        },
        {
            'question_text': 'How can a CRO help increase company reputation internationally? (rz8w4n6t)',
            'option_a': 'By delaying communication',
            'option_b': 'By overpromising',
            'option_c': 'By ignoring clients',
            'option_d': 'By giving accurate information and excellent service',
            'correct_option': 'D'
        },
        {
            'question_text': 'Which of the following shows the best CRO performance? (sw2w9q5k)',
            'option_a': 'Satisfied clients, timely responses, and accurate reporting',
            'option_b': 'Missing files and angry clients',
            'option_c': 'No record keeping',
            'option_d': 'Late updates',
            'correct_option': 'A'
        }
    ],
    'Project Manager': [
        {
            'question_text': 'What is the main responsibility of a Project Manager in the translation department? (kx7x4m9t)',
            'option_a': 'Translating documents personally',
            'option_b': 'Overseeing translation projects from start to finish',
            'option_c': 'Designing company brochures',
            'option_d': 'Managing office security',
            'correct_option': 'B'
        },
        {
            'question_text': 'What should the Project Manager check before starting a new project? (lw5w8t7q)',
            'option_a': 'Client requirements and language pair',
            'option_b': 'Translator\'s lunch break',
            'option_c': 'Office decoration',
            'option_d': 'Computer wallpaper',
            'correct_option': 'A'
        },
        {
            'question_text': 'Which team does the Project Manager coordinate with daily? (my8w2p6n)',
            'option_a': 'Security guards',
            'option_b': 'Drivers',
            'option_c': 'Translators and Operations Officers',
            'option_d': 'Cleaners',
            'correct_option': 'C'
        },
        {
            'question_text': 'What is the first step after receiving a new client request? (nw1w5q8t)',
            'option_a': 'Create a project file and assign a translator',
            'option_b': 'Wait for the client to call back',
            'option_c': 'Forward it to another department',
            'option_d': 'Delay it for one week',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the key skill for a Translation Project Manager? (pw3w7m9r)',
            'option_a': 'Communication and time management',
            'option_b': 'Typing fast',
            'option_c': 'Accounting',
            'option_d': 'Photography',
            'correct_option': 'A'
        },
        {
            'question_text': 'If a translator delays the project, what should the Project Manager do? (qx6w9t2p)',
            'option_a': 'Cancel the project',
            'option_b': 'Contact translator and adjust the schedule',
            'option_c': 'Ignore the issue',
            'option_d': 'Inform no one',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the main goal of project management in translation? (rw8w1p5n)',
            'option_a': 'Deliver accurate translations on time',
            'option_b': 'Increase project cost',
            'option_c': 'Ignore client instructions',
            'option_d': 'Delay reports',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the purpose of a project tracker or log? (sw2w4m7t)',
            'option_a': 'To monitor deadlines and progress',
            'option_b': 'To record lunch breaks',
            'option_c': 'To manage office supplies',
            'option_d': 'To calculate salaries',
            'correct_option': 'A'
        },
        {
            'question_text': 'If a client changes project details midway, what should be done? (ty5w6q3r)',
            'option_a': 'Cancel project',
            'option_b': 'Ignore the change',
            'option_c': 'Update records and inform translator immediately',
            'option_d': 'Continue with old details',
            'correct_option': 'C'
        },
        {
            'question_text': 'What is an important communication skill for a Project Manager? (uw7w8n5k)',
            'option_a': 'Listening actively and responding clearly',
            'option_b': 'Talking continuously',
            'option_c': 'Avoiding feedback',
            'option_d': 'Using difficult language',
            'correct_option': 'A'
        },
        {
            'question_text': 'Which software or tool helps manage multiple translation projects? (vw1w2t9p)',
            'option_a': 'Excel, Google Sheets, or CRM systems',
            'option_b': 'Photoshop',
            'option_c': 'PowerPoint',
            'option_d': 'Media Player',
            'correct_option': 'A'
        },
        {
            'question_text': 'What should the Project Manager do before sending the final translation to the client? (ww3w4m6q)',
            'option_a': 'Review for accuracy and formatting',
            'option_b': 'Change the translator\'s name',
            'option_c': 'Print without checking',
            'option_d': 'Skip proofreading',
            'correct_option': 'A'
        },
        {
            'question_text': 'What should be done if a translator submits poor-quality work? (xx6w7p1n)',
            'option_a': 'Approve it anyway',
            'option_b': 'Send it back for revision and note in record',
            'option_c': 'Delete it',
            'option_d': 'Hide it from client',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is "client feedback" used for? (yw8w9q2t)',
            'option_a': 'To improve future translation services',
            'option_b': 'To delete client data',
            'option_c': 'To end communication',
            'option_d': 'To delay payments',
            'correct_option': 'A'
        },
        {
            'question_text': 'What is the Project Manager\'s role during translator appointment scheduling? (zz2w3m5r)',
            'option_a': 'Skip confirmation',
            'option_b': 'Book anyone randomly',
            'option_c': 'Leave it to client',
            'option_d': 'Ensure suitable translator is booked at the right time',
            'correct_option': 'D'
        },
        {
            'question_text': 'Which department supports the Project Manager directly? (hw5w6t8p)',
            'option_a': 'Operations Team',
            'option_b': 'Cleaning Staff',
            'option_c': 'Security Team',
            'option_d': 'IT Department only',
            'correct_option': 'A'
        },
        {
            'question_text': 'How can the Project Manager handle urgent translation requests? (jw7w8p4n)',
            'option_a': 'Prioritize, reassign, and manage resources quickly',
            'option_b': 'Refuse all urgent work',
            'option_c': 'Delay it purposely',
            'option_d': 'Send without checking',
            'correct_option': 'A'
        },
        {
            'question_text': 'What does "project delivery deadline" mean? (kx9w1q6r)',
            'option_a': 'The day client visits the office',
            'option_b': 'The date by which the translation must be completed',
            'option_c': 'Translator\'s off day',
            'option_d': 'Monthly salary date',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the best way to ensure translation accuracy? (lw2w5m8t)',
            'option_a': 'Quality check and proofreading before submission',
            'option_b': 'Sending raw translation',
            'option_c': 'Ignoring grammar',
            'option_d': 'Relying only on machine translation',
            'correct_option': 'A'
        },
        {
            'question_text': 'What should the Project Manager do after project completion? (my4w7q1p)',
            'option_a': 'Forget about client feedback',
            'option_b': 'Delete all communication',
            'option_c': 'Record project summary and close the file',
            'option_d': 'Start new project immediately',
            'correct_option': 'C'
        },
        {
            'question_text': 'Why is communication with translators important? (nw7w9t3k)',
            'option_a': 'To clarify instructions and avoid errors',
            'option_b': 'To waste time',
            'option_c': 'To check their personal matters',
            'option_d': 'To give them marketing tasks',
            'correct_option': 'A'
        },
        {
            'question_text': 'Which document is created at the beginning of every project? (pw9w1m4r)',
            'option_a': 'Project brief or client instruction sheet',
            'option_b': 'Invoice only',
            'option_c': 'ID copy',
            'option_d': 'Blank form',
            'correct_option': 'A'
        },
        {
            'question_text': 'If a translator requests more time, what should the manager do? (qz1w2p6n)',
            'option_a': 'Replace without notice',
            'option_b': 'Refuse without discussion',
            'option_c': 'Ignore request',
            'option_d': 'Review reason and update client accordingly',
            'correct_option': 'D'
        },
        {
            'question_text': 'What is the benefit of maintaining client records properly? (rw3w4t8k)',
            'option_a': 'For follow-ups, reporting, and service quality',
            'option_b': 'To delete data easily',
            'option_c': 'To confuse staff',
            'option_d': 'To reduce transparency',
            'correct_option': 'A'
        },
        {
            'question_text': 'What quality makes a Project Manager successful? (sw6w7m2p)',
            'option_a': 'Leadership, organization, and responsibility',
            'option_b': 'Laziness',
            'option_c': 'Ignoring deadlines',
            'option_d': 'Delegating without follow-up',
            'correct_option': 'A'
        }
    ],
    'Airless Intumescent / Cementitious Sprayer': [
        {
            'question_text': 'What is the primary purpose of an intumescent coating? (kxx7m4t9)',
            'option_a': 'Decorative finish',
            'option_b': 'Fire protection by expanding under heat',
            'option_c': 'Water resistance only',
            'option_d': 'Preventing rust only',
            'correct_option': 'B'
        },
        {
            'question_text': 'At what temperature do most intumescent coatings typically begin to expand? (myz5p8r1)',
            'option_a': '50–80°C',
            'option_b': '150–200°C',
            'option_c': '250–300°C',
            'option_d': '400–450°C',
            'correct_option': 'C'
        },
        {
            'question_text': 'Which equipment is used for applying intumescent coatings with high viscosity? (nxy9t2k6)',
            'option_a': 'Gravity spray gun',
            'option_b': 'Airless spray machine',
            'option_c': 'Brush and roller',
            'option_d': 'HVLP sprayer',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the ideal nozzle size for spraying thick-film intumescent coatings? (pzy3m6t8)',
            'option_a': '117',
            'option_b': '317',
            'option_c': '521',
            'option_d': '635',
            'correct_option': 'D'
        },
        {
            'question_text': 'Which factor most affects the dry film thickness (DFT)? (syx6p4r2)',
            'option_a': 'Color shade of coating',
            'option_b': 'Ambient sound',
            'option_c': 'Pump pressure and nozzle size',
            'option_d': 'Worker’s age',
            'correct_option': 'C'
        },
        {
            'question_text': 'Why is wet film thickness (WFT) measurement required? (twz8n1k5)',
            'option_a': 'To calculate final DFT after drying',
            'option_b': 'For color consistency',
            'option_c': 'To reduce coating usage',
            'option_d': 'To check surface area',
            'correct_option': 'A'
        },
        {
            'question_text': 'Which tool is used to measure Dry Film Thickness? (uxy2m7t3)',
            'option_a': 'Vernier caliper',
            'option_b': 'Ultrasonic thickness gauge',
            'option_c': 'Spirit level',
            'option_d': 'Pipe gauge',
            'correct_option': 'B'
        },
        {
            'question_text': 'Cementitious fireproofing is usually applied using: (vxy5p3r6)',
            'option_a': 'Trowel only',
            'option_b': 'Airless pump with wet-mix system',
            'option_c': 'Brush',
            'option_d': 'Roller',
            'correct_option': 'B'
        },
        {
            'question_text': 'Before spraying intumescent coating, surface profile must be checked according to: (wwx7n9k2)',
            'option_a': 'SSPC standards',
            'option_b': 'AWS standards',
            'option_c': 'OSHA standards',
            'option_d': 'NFPA electrical code',
            'correct_option': 'A'
        },
        {
            'question_text': 'Which environmental condition MOST affects coating curing? (xxy1m5t8)',
            'option_a': 'Moonlight',
            'option_b': 'Humidity and temperature',
            'option_c': 'Sound vibration',
            'option_d': 'Worker’s clothing',
            'correct_option': 'B'
        },
        {
            'question_text': 'What happens if intumescent coating is applied too thick in a single pass? (yxy4p6r1)',
            'option_a': 'Better finish',
            'option_b': 'Cracking and sagging',
            'option_c': 'Faster drying',
            'option_d': 'Increased adhesion',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the purpose of primer before intumescent application? (zxy6n8k3)',
            'option_a': 'Reduce spray pressure',
            'option_b': 'Provide corrosion resistance and adhesion',
            'option_c': 'Change texture',
            'option_d': 'Speed up fire rating',
            'correct_option': 'B'
        },
        {
            'question_text': 'Which fire rating is commonly required in Qatar for steel structures? (kyy9t2m5)',
            'option_a': '15 minutes',
            'option_b': '30 minutes',
            'option_c': '60–120 minutes',
            'option_d': '5 hours',
            'correct_option': 'C'
        },
        {
            'question_text': 'For cementitious coating mixing, water ratio must be: (lxy1m4t7)',
            'option_a': 'Random',
            'option_b': 'As recommended by manufacturer',
            'option_c': 'More water for faster spray',
            'option_d': 'Less water for harder finish',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the main danger of spraying in closed areas without ventilation? (myy3p7r9)',
            'option_a': 'High electricity usage',
            'option_b': 'Overspray mess',
            'option_c': 'Inhalation of hazardous fumes',
            'option_d': 'Equipment noise',
            'correct_option': 'C'
        },
        {
            'question_text': 'Intumescent coatings must be stored at: (nyy5t1k2)',
            'option_a': 'Any temperature',
            'option_b': 'Below freezing',
            'option_c': 'Recommended room temperature',
            'option_d': 'Direct sunlight',
            'correct_option': 'C'
        },
        {
            'question_text': 'During spraying, pump pressure should be adjusted to: (pxy8m6t4)',
            'option_a': 'Reduce noise',
            'option_b': 'Avoid overspray and maintain correct film build',
            'option_c': 'Match operator’s preference',
            'option_d': 'Prevent hose vibration',
            'correct_option': 'B'
        },
        {
            'question_text': 'Cementitious fireproofing is mostly applied on: (sxy2p5r7)',
            'option_a': 'Aluminum sheets',
            'option_b': 'Structural steel and concrete',
            'option_c': 'Wooden furniture',
            'option_d': 'Plastic pipes',
            'correct_option': 'B'
        },
        {
            'question_text': 'What is the main function of mesh reinforcement in cementitious fireproofing? (tyy4n7k9)',
            'option_a': 'Decoration',
            'option_b': 'Reduce thickness',
            'option_c': 'Control cracks and increase strength',
            'option_d': 'Change color',
            'correct_option': 'C'
        },
        {
            'question_text': 'When spraying intumescent coating, overlapping pattern should be: (uyy7m3t1)',
            'option_a': 'Random',
            'option_b': 'Zig-zag',
            'option_c': '50% overlap for uniformity',
            'option_d': 'No overlap',
            'correct_option': 'C'
        },
        {
            'question_text': 'What safety gear is mandatory during spraying? (vxy9p1r3)',
            'option_a': 'Cap only',
            'option_b': 'Full PPE: respirator, goggles, gloves',
            'option_c': 'Sandals',
            'option_d': 'Cotton mask',
            'correct_option': 'B'
        },
        {
            'question_text': 'What happens if DFT is below the required thickness? (wxy2n4k6)',
            'option_a': 'Better look',
            'option_b': 'Fire rating will fail',
            'option_c': 'Less weight',
            'option_d': 'Saves material',
            'correct_option': 'B'
        },
        {
            'question_text': 'Which type of airless pump is best for intumescent coatings? (xwy4m6t8)',
            'option_a': 'Graco or WIWA high-pressure pump',
            'option_b': 'Low-pressure pump',
            'option_c': 'Manual hand sprayer',
            'option_d': 'Car paint sprayer',
            'correct_option': 'A'
        },
        {
            'question_text': 'Why is substrate temperature important? (yxy7p2r4)',
            'option_a': 'For worker comfort',
            'option_b': 'To avoid condensation and coating failure',
            'option_c': 'For better shine',
            'option_d': 'For noise reduction',
            'correct_option': 'B'
        },
        {
            'question_text': 'After spraying cementitious coating, curing is usually done by: (zxy9n5k7)',
            'option_a': 'Direct heat',
            'option_b': 'Water misting',
            'option_c': 'Sand blasting',
            'option_d': 'Air drying only',
            'correct_option': 'B'
        }
    ],
}

def seed_questions():
    '''Seed the database with MCQ questions'''
    app = create_app()
    
    with app.app_context():
        print('Starting database seeding...')
        
        # Clear existing questions (optional - comment out if you want to keep existing data)
        Question.query.delete()
        
        # Insert questions for each role
        total_inserted = 0
        for role, questions in MCQ_DATA.items():
            print(f'\nSeeding questions for {role}...')
            for q_data in questions:
                question = Question(
                    role=role,
                    question_text=q_data['question_text'],
                    option_a=q_data['option_a'],
                    option_b=q_data['option_b'],
                    option_c=q_data['option_c'],
                    option_d=q_data['option_d'],
                    correct_option=q_data['correct_option']
                )
                db.session.add(question)
                total_inserted += 1
            print(f'✓ Added {len(questions)} questions for {role}')
        
        # Create admin user if not exists
        admin = User.query.filter_by(email='admin@skilltest.com').first()
        if not admin:
            print('\nCreating admin user...')
            admin = User(
                name='Admin',
                email='admin@skilltest.com',
                role='Admin',
                is_admin=True
            )
            admin.set_password('admin123')
            db.session.add(admin)
            print('✓ Admin user created')
        else:
            print('\n✓ Admin user already exists')
        
        db.session.commit()
        print(f'\n✅ Successfully seeded {total_inserted} questions!')
        print('\nAdmin credentials:')
        print('Email: admin@skilltest.com')
        print('Password: admin123')

if __name__ == '__main__':
    seed_questions()