<template>
  <div class="app container-fluid pt-2">

    <h2 class="alert alert-warning">Django5 & Vue.JS3 & Bootstrap => CRUD Application</h2>

    <div class="row">
      <div class="col-md-7">
        <h2 class="alert alert-success">Liste des Etudiants</h2>

        <table class="table table-bordered mt-4">
          <thead>
            <tr>
              <th scope="col">Nom</th>
              <th scope="col">Cours</th>
              <th scope="col">Email</th>
              <th scope="col">Genre</th>
              <th scope="col">Action</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="student in students" :key="student.id">
              <td>{{ student.nom }}</td>
              <td>{{ student.cours }}</td>
              <td>{{ student.email }}</td>
              <td>{{ student.genre }}</td>
              <td>
                <a href="#" class="edit" title="">
                  <button class="btn btn-warning btn-sm me-2" @click="editBtn(student.id)">Edit</button>
                </a>
                <a href="#" class="edit ml-1" title="">
                  <button class="btn btn-danger btn-sm"  @click="deleteStudent(student.id)">Delete</button>
                </a>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="col-md-5 addEdit">

        <!-- There is a current student to be edited -->
        <div v-if="Object.keys(currentStudent).length !== 0">

          <h2 class="alert alert-warning">Editer un Etudiant</h2>
          
          <form @submit.prevent="updateStudent(currentStudent.id)">
            <div class="row">
              <div class="col">
                <div class="form-group">
                  <label class="form-label float-start">Nom</label>
                  <input type="text" class="form-control" v-model="currentStudent.nom">
                </div>
              </div>

              <div class="col">
                <div class="form-group">
                  <label class="form-label float-start">Email</label>
                  <input type="email" class="form-control"
                  v-model="currentStudent.email">
                </div>
              </div>
            </div>

            <div class="row">
              <div class="col">
                <div class="form-group">
                  <label class="form-label float-start">Cours</label>
                  <input type="text" class="form-control" v-model="currentStudent.cours">
                </div>
              </div>
              <div class="col">

                <div class="form-group">
                  <label class="form-label float-start">Genre</label>
                  <input type="text" class="form-control"
                  v-model="currentStudent.genre">
                </div>
              </div>

            </div>
            <button type="submit" class="btn btn-warning float-start col-md-4 mt-2">Modifier</button>
          </form>
        </div>

        <!-- There is no current student to be edited -->
        <div v-else>
          
          <h2 class="alert alert-info">Ajouter un Etudiant</h2>

          <form @submit.prevent="saveStudent()">
            <div class="row">
              <div class="col">
                <div class="form-group">
                  <label class="form-label float-start">Nom</label>
                  <!-- 
                    v-model est une directive dans Vue.js qui permet de créer une liaison bidirectionnelle entre un champ de formulaire HTML (comme un <input>, <textarea>, ou <select>) et une propriété dans le modèle de données Vue
                   -->
                  <input type="text" class="form-control" v-model="student.nom">
                </div>
              </div>

              <div class="col">
                <div class="form-gro up">
                  <label class="form-label float-start">Email</label>
                  <input type="email" class="form-control" v-model="student.email">
                </div>
              </div>
            </div>

            <div class="row">
              <div class="col">
                <div class="form-group">
                  <label class="form-label float-start">Cours</label>
                  <input type="text" class="form-control" v-model="student.cours">
                </div>
              </div>
              <div class="col">
                <div class="form-group">
                  <label class="form-label float-start">Genre</label>
                  <input type="text" class="form-control" v-model="student.genre">
                </div>
              </div>

            </div>
            <button type="submit" class="btn btn-success col-md-4 float-start mt-3">Ajouter</button>
          </form>
        </div>
      </div>

    </div>
  </div>
</template>

<!-- <script>
import axios from 'axios';


export default {
  data() {
    return {
      'api': 'http://127.0.0.1:8000/api/',
      'student': {
        'nom': '',
        'cours': '',
        'email': '',
        'genre': ''
      },
    }
  },

  mounted() {
    console.log("Dom mounted");
  },

  created() {
    console.log("Dom created"); // Dom will be created befor mounted
    this.getStudents()
  },

  methods: {
    getStudents() {
      console.log("listes etudiants");
    }
  }
}

</script> -->

// version vueJS 3.2 et +
<script setup>
import { ref, onMounted, onBeforeMount, reactive } from 'vue';
import axios from 'axios';

const student = ref({
  nom: '',
  cours: '',
  email: '',
  genre: ''
});

// ref == l'equivalent de useState dans react
const students = ref([]);
const api = 'http://127.0.0.1:8000/api';

// Créez une référence réactive pour currentStudent
const currentStudent = ref({});

const getStudents = () => {
  console.log("Liste des étudiants");
  axios.get(api + '/students/')
    .then(
      response => {
        console.log(response.data);
        students.value = response.data;
      }
    ).catch(error => {
      console.log(error);
    })
};

const saveStudent = () => {
  axios.post(api + '/students/', student.value)
    .then(
      response => {
        console.log(response.data);
        getStudents()
        // Réinitialisez tous les champs de l'objet student
        student.value = {};
      }
    ).catch(error => {
      console.log(error);
    })
};

const editBtn = (id) => {
  const foundStudent = students.value.find(student => student.id === id);

  if (foundStudent) {
    console.log(foundStudent.nom);

    // Mettez à jour les propriétés de currentStudent
    currentStudent.value = { ...foundStudent };

    // currentStudent = { 'id': foundStudent.id, 'nom': foundStudent.nom, 'cours': foundStudent.cours, 'email': foundStudent.email, 'genre': foundStudent.genre }
  }
};

const updateStudent = (id) => {
  axios.put(api + `/students/${id}/`, currentStudent.value)
    .then(
      response => {
        console.log(response.data);
        getStudents()
        // Réinitialisez tous les champs de l'objet student
        currentStudent.value = {};
      }
    ).catch(error => {
      console.log(error);
    })
};

const deleteStudent = (id) => {
  axios.delete(api + `/students/${id}/`)
    .then(
      response => {
        console.log(response.data);
        getStudents()
      }
    ).catch(error => {
      console.log(error);
    })
};

onMounted(() => {
  console.log("Le DOM est monté");
  console.log(Object.keys(currentStudent.value).length);
});

onBeforeMount(() => {
  console.log("Le DOM est créé avant le montage");
  getStudents();
});
</script>

<style scoped>
.addEdit {
  display: flex;
  flex-direction: column;
  gap: 0rem;
}

label {
  padding: 2px;
  margin-top: .5rem;
  border-radius: 5px;
  background: #6fc3d6;
  color: rgb(19, 20, 19);
}
</style>