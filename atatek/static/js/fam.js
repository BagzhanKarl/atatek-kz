//JavaScript
var options = getOptions();

var family = new FamilyTree(document.getElementById('tree'), {
    mouseScrool: FamilyTree.scroll,
    scaleInitial: options.scaleInitial,
    enableSearch: false,
    mode: 'light',
    template: 'hugo',
    nodeMenu: {
        edit: { text: 'Өзгерту' },
        details: { text: 'Ақпарат' },
    },
    nodeTreeMenu: false,
    nodeBinding: {
        field_0: 'name',
        field_1: 'born',
        fiels_2: 'surname'
    },
    editForm: {
        titleBinding: "name",
        generateElementsFromFields: false,
        elements: [
            { type: 'textbox', label: 'Есімі', binding: 'name' },
            { type: 'textbox', label: 'Тегі', binding: 'surname' },

            [
                { type: 'textbox', label: 'Телефон номері', binding: 'phone' },
                { type: 'date', label: 'Туған күні', binding: 'born' }
            ],
        ]
    },
});

family.on('field', function (sender, args) {
    if (args.name == 'born') {
        var date = new Date(args.value);
        args.value = date.toLocaleDateString();
    }
});


family.load([
    { id: 1, pids: [2], gender: 'male', name: 'Карл', surname: 'Оңғаров', born: null, city: 'Алматы облысы, Кеген ауданы, Тасашы', alive: 'no' },
    { id: 2, pids: [1], gender: 'female', name: 'Гулсара', surname: 'Тастанқызы', born: null, alive: 'no' },
    { id: 3, pids: [4], gender: 'male', name: 'Самат', surname: 'Оңғаров', born: '1977-11-01', city: 'Алматы облысы, Кеген ауданы, Кеген', alive: 'yes', fid: 1, mid: 2 },
    { id: 4, pids: [3], gender: 'female', name: 'Нұрбақыт', surname: 'Оңғарова', born: '1978-03-10', city: 'Алматы облысы, Кеген ауданы, Ақтасты', alive: 'yes' },
    { id: 5, gender: 'male', name: 'Багжан Карл', surname: 'Карл', born: null, alive: 'yes', fid: 3, mid: 4 },
]);


function getOptions(){
    const searchParams = new URLSearchParams(window.location.search);
    var fit = searchParams.get('fit');
    var enableSearch = false;
    var scaleInitial = 0.8;
    if (fit == 'yes'){
        scaleInitial = FamilyTree.match.boundary;
    }
    return {enableSearch, scaleInitial};
}