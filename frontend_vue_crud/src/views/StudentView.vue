<template>
  <div class="app container-fluid">

    <h2 class="alert alert-warning mt-2">Django5 & Vue.JS3 & Bootstrap => CRUD Application</h2>

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
            <tr>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td>
                <a href="#" class="edit" title="">
                  <button class="btn btn-warning btn-sm me-2">Edit</button>
                </a>
                <a href="#" class="edit ml-1" title="">
                  <button class="btn btn-danger btn-sm">Delete</button>
                </a>
              </td>
            </tr>
          </tbody>
        </table>

      </div>

      <div class="col-md-5 addEdit">
        <!-- There is a current student to be edited -->
        <div class="">
          <h2 class="alert alert-warning">Editer un Etudiant</h2>
          <form>
            <div class="row">
              <div class="col">
                <div class="form-group">
                  <label class="form-label float-start">Nom</label>
                  <input type="text" class="form-control">
                </div>
              </div>

              <div class="col">
                <div class="form-group">
                  <label class="form-label float-start">Email</label>
                  <input type="email" class="form-control">
                </div>
              </div>
            </div>

            <div class="row">
              <div class="col">
                <div class="form-group">
                  <label class="form-label float-start">Cours</label>
                  <input type="text" class="form-control">
                </div>
              </div>
              <div class="col">

                <div class="form-group">
                  <label class="form-label float-start">Genre</label>
                  <input type="text" class="form-control">
                </div>
              </div>

            </div>
            <button type="submit" class="btn btn-warning float-start col-md-4 mt-2">Modifier</button>
          </form>
        </div>

        <!-- There is no current student to be edited -->
        <div class="">
          <h2 class="alert alert-info">Ajouter un Etudiant</h2>
          <form>
            <div class="row">
              <div class="col">
                <div class="form-group">
                  <label class="form-label float-start">Nom</label>
                  <input type="text" class="form-control">
                </div>
              </div>

              <div class="col">
                <div class="form-group">
                  <label class="form-label float-start">Email</label>
                  <input type="email" class="form-control">
                </div>
              </div>
            </div>

            <div class="row">
              <div class="col">
                <div class="form-group">
                  <label class="form-label float-start">Cours</label>
                  <input type="text" class="form-control">
                </div>
              </div>
              <div class="col">
                <div class="form-group">
                  <label class="form-label float-start">Genre</label>
                  <input type="text" class="form-control">
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

<script setup>
console.log("vue js");
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