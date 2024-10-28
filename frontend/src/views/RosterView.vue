<script setup lang="ts"></script>

<template>
  <div class="columns mb-4">
    <div class="column">
      <div class="file is-info">
        <label class="file-label">
          <input class="file-input" type="file" name="resume" />
          <span class="file-cta">
            <span class="file-label"> Import Roster </span>
          </span>
        </label>
      </div>
    </div>

    <div class="column">
      <div class="select">
        <select disabled>
          <option>Imperial Knights</option>
        </select>
      </div>
    </div>
    <div class="column">
      <div class="select">
        <select disabled>
          <option>Noble Lance</option>
        </select>
      </div>
    </div>
    <div class="column">
      <div class="select">
        <select>
          <option>Select Points</option>
          <option>1000</option>
          <option>2000</option>
          <option>3000</option>
        </select>
      </div>
    </div>
    <div class="column is-3"><input class="input" type="text" placeholder="Roster Name" /></div>
    <div class="column">
      <a class="button is-success" href="path_to_file" download="test.txt">Export Roster</a>
    </div>
  </div>
  <div class="columns is-centered mb-5">
    <div class="column is-6">
      <span class="has-text-centered"> <p>1530/2000</p> </span>
      <progress class="progress is-small is-dark" value="1530" max="2000"></progress>
    </div>
  </div>

  <div class="columns">
    <div class="column is-4 has-text-centered">
      <nav class="panel">
        <p class="panel-heading">CHARACTER</p>

        <a class="panel-block is-justify-content-space-between">
          <span class="has-text-weight-semibold">Canis Rex</span>
          <div class="tags">
            <span class="tag is-light">Warlord</span>
            <span class="tag is-pulled-right is-light">460 points</span>
            <span class="tag is-delete is-light"></span>
          </div>
        </a>
        <div class="has-background-white-ter pt-2 pb-2">
          <div class="content has-text-left">
            <p class="is-size-7 pl-5">
              1x Chainbreaker las-impulsor
              <br />
              1x Chainbreaker multi-laser
              <br />
              1x Freedom's Hand
            </p>
          </div>
        </div>

        <a class="panel-block is-justify-content-space-between">
          <span class="has-text-weight-semibold">Knight Paladin</span>
          <div class="tags">
            <span class="tag is-pulled-right is-light">440 points</span>
            <span class="tag is-delete is-light"></span>
          </div>
        </a>
        <div class="has-background-white-ter pt-2 pb-2">
          <div class="content has-text-left">
            <p class="is-size-7 pl-5">
              1x Icarus autocannons
              <br />
              1x Questoris heavy stubber
              <br />
              1x Rapid-fire battle cannon
              <br />
              1x Reaper chainsword
              <br />
              <span class="has-text-weight-semibold">Enhancement:</span> Unyielding paragon
            </p>
          </div>
        </div>
      </nav>
      <span class="buttons is-centered">
        <button class="button is-small is-outlined">Add Character</button>
        <button class="button is-small is-outlined">Add Enhancement</button>
      </span>
    </div>
    <div class="column is-4 has-text-centered">
      <nav class="panel">
        <p class="panel-heading">BATTLELINE</p>
        <a class="panel-block is-justify-content-space-between">
          <span class="has-text-weight-semibold">Armiger Helverin</span>
          <div class="tags">
            <span class="tag is-pulled-right is-light">150 points</span>
            <span class="tag is-delete is-light"></span>
          </div>
        </a>
        <a class="panel-block is-justify-content-space-between">
          <span class="has-text-weight-semibold">Armiger Helverin</span>
          <div class="tags">
            <span class="tag is-pulled-right is-light">150 points</span>
            <span class="tag is-delete is-light"></span>
          </div>
        </a>
        <a class="panel-block is-justify-content-space-between">
          <span class="has-text-weight-semibold">Armiger Warglaive</span>
          <div class="tags">
            <span class="tag is-pulled-right is-light">150 points</span>
            <span class="tag is-delete is-light"></span>
          </div>
        </a>
        <a class="panel-block is-justify-content-space-between">
          <span class="has-text-weight-semibold">Armiger Warglaive</span>
          <div class="tags">
            <span class="tag is-pulled-right is-light">150 points</span>
            <span class="tag is-delete is-light"></span>
          </div>
        </a>
        <div class="has-background-white-ter pt-2 pb-2">
          <div class="content has-text-left">
            <p class="is-size-7 pl-5">
              1x Questoris heavy stubber
              <br />
              1x Thermal spear
              <br />
              1x Reaper chain-cleaver
            </p>
          </div>
        </div>

        <a class="panel-block is-justify-content-space-between">
          <span class="has-text-weight-semibold">Armiger Warglaive</span>
          <div class="tags">
            <span class="tag is-pulled-right is-light">150 points</span>
            <span class="tag is-delete is-light"></span>
          </div>
        </a>
        <a class="panel-block is-justify-content-space-between">
          <span class="has-text-weight-semibold">Armiger Warglaive</span>
          <div class="tags">
            <span class="tag is-pulled-right is-light">150 points</span>
            <span class="tag is-delete is-light"></span>
          </div>
        </a>
        <a class="panel-block is-justify-content-space-between">
          <span class="has-text-weight-semibold">Armiger Warglaive</span>
          <div class="tags">
            <span class="tag is-pulled-right is-light">150 points</span>
            <span class="tag is-delete is-light"></span>
          </div>
        </a>
      </nav>
      <button class="button is-small is-outlined">Add Battleline Unit</button>
    </div>
    <div class="column is-4 has-text-centered">
      <nav class="panel">
        <p class="panel-heading">ALLIED UNIT</p>
        <a class="panel-block is-justify-content-space-between">
          <span class="has-text-weight-semibold">Callidus Assassin</span>
          <div class="tags">
            <span class="tag is-pulled-right is-light">90 points</span>
            <span class="tag is-delete is-light"></span>
          </div>
        </a>
        <a class="panel-block is-justify-content-space-between">
          <span class="has-text-weight-semibold">Vindicare Assassin</span>
          <div class="tags">
            <span class="tag is-pulled-right is-light">80 points</span>
            <span class="tag is-delete is-light"></span>
          </div>
        </a>
        <a class="panel-block is-justify-content-space-between">
          <span class="has-text-weight-semibold">Exaction Squad</span>
          <div class="tags">
            <span class="tag is-pulled-right is-light">110 points</span>
            <span class="tag is-delete is-light"></span>
          </div>
        </a>
        <div class="has-background-white-ter pt-2 pb-2">
          <div class="content has-text-left">
            <p class="is-size-7 pl-5">
              <span class="has-text-weight-semibold">1x Proctor-Exactant</span>
              <br />
              <span class="ml-3"></span>1x Arbites combat shotgun
              <br />
              <span class="ml-3"></span> 1x Arbites shotpistol
              <br />
              <span class="ml-3"></span> 1x Close combat weapon

              <br />
              <span class="has-text-weight-semibold">9x Exaction Vigilant</span>
              <br />
              <span class="ml-3"></span>7x Arbites combat shotgun
              <br />
              <span class="ml-3"></span>1x Arbites grenade launcher
              <br />

              <span class="ml-3"></span> 9x Arbites shotpistol
              <br />
              <span class="ml-3"></span> 9x Close combat weapon

              <br />
              <span class="ml-3"></span> 1x Heavy stubber

              <br />

              <span class="has-text-weight-semibold">1x Cyber-mastiff</span>
              <br />
              <span class="ml-3"></span>1x Mechanical bite
            </p>
          </div>
        </div>
      </nav>

      <button class="button is-small is-outlined" disabled>Add Allied Unit</button>
    </div>
  </div>
  <div class="modal">
    <div class="modal-background"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">Add Character</p>
        <button class="delete" aria-label="close"></button>
      </header>
      <section class="modal-card-body">
        <div class="panel-block">
          <p class="control has-icons-left">
            <input class="input" type="text" placeholder="Search" />
            <span class="icon is-left">
              <i class="fas fa-search" aria-hidden="true"></i>
            </span>
          </p>
        </div>
        <a class="panel-block is-justify-content-space-between">
          <span class="has-text-weight-semibold">Canis Rex</span>
          <div class="tags">
            <span class="tag is-pulled-right is-light">460 points</span>
          </div>
        </a>
        <a class="panel-block is-justify-content-space-between">
          <span class="has-text-weight-semibold">Canis Rex</span>
          <div class="tags">
            <span class="tag is-pulled-right is-light">460 points</span>
          </div>
        </a>
        <a class="panel-block is-justify-content-space-between">
          <span class="has-text-weight-semibold">Canis Rex</span>
          <div class="tags">
            <span class="tag is-pulled-right is-light">460 points</span>
          </div>
        </a>
        <a class="panel-block is-justify-content-space-between">
          <span class="has-text-weight-semibold">Canis Rex</span>
          <div class="tags">
            <span class="tag is-pulled-right is-light">460 points</span>
          </div>
        </a>
        <a class="panel-block is-justify-content-space-between">
          <span class="has-text-weight-semibold">Canis Rex</span>
          <div class="tags">
            <span class="tag is-pulled-right is-light">460 points</span>
          </div>
        </a>
        <a class="panel-block is-justify-content-space-between">
          <span class="has-text-weight-semibold">Canis Rex</span>
          <div class="tags">
            <span class="tag is-pulled-right is-light">460 points</span>
          </div>
        </a>
        <a class="panel-block is-justify-content-space-between">
          <span class="has-text-weight-semibold">Canis Rex</span>
          <div class="tags">
            <span class="tag is-pulled-right is-light">460 points</span>
          </div>
        </a>
        <a class="panel-block is-justify-content-space-between">
          <span class="has-text-weight-semibold">Canis Rex</span>
          <div class="tags">
            <span class="tag is-pulled-right is-light">460 points</span>
          </div>
        </a>
        <a class="panel-block is-justify-content-space-between">
          <span class="has-text-weight-semibold">Canis Rex</span>
          <div class="tags">
            <span class="tag is-pulled-right is-light">460 points</span>
          </div>
        </a>
        <a class="panel-block is-justify-content-space-between">
          <span class="has-text-weight-semibold">Canis Rex</span>
          <div class="tags">
            <span class="tag is-pulled-right is-light">460 points</span>
          </div>
        </a>
        <a class="panel-block is-justify-content-space-between">
          <span class="has-text-weight-semibold">Canis Rex</span>
          <div class="tags">
            <span class="tag is-pulled-right is-light">460 points</span>
          </div>
        </a>
        <a class="panel-block is-justify-content-space-between">
          <span class="has-text-weight-semibold">Canis Rex</span>
          <div class="tags">
            <span class="tag is-pulled-right is-light">460 points</span>
          </div>
        </a>
        <a class="panel-block is-justify-content-space-between">
          <span class="has-text-weight-semibold">Canis Rex</span>
          <div class="tags">
            <span class="tag is-pulled-right is-light">460 points</span>
          </div>
        </a>
        <a class="panel-block is-justify-content-space-between">
          <span class="has-text-weight-semibold">Canis Rex</span>
          <div class="tags">
            <span class="tag is-pulled-right is-light">460 points</span>
          </div>
        </a>
      </section>

      <footer class="modal-card-foot">
        <button class="button is-success">Save changes</button>
        <button class="button">Cancel</button>
      </footer>
    </div>
  </div>
</template>

<style lang="scss">
.noHover {
  pointer-events: none;
}
</style>
