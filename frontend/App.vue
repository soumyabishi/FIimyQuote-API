<template>
    <div class="quote-wrapper">


        <a href="javascript:void(0)" class="logo-container" v-on:click="get_quote()" v-shortkey="['space']" @shortkey="get_quote()">
            <img alt="FilmyQuote" src="./assets/img/logo.svg">
        </a>

        <p class="made-by ibm-type-mono">
            Made with love by <a href="http://github.com/soumyabishi">Soumya</a> & <a href="#">Shiv</a>.
        </p>


        <p class="overlay-text">FilmyQuote</p>

        <div class="something-semantic">
            <div class="something-else-semantic">

                <div class="ui container">


                    <section class="loader" v-if="loading_quote">
                        <div id="wrap">
                            <div id="loader">
                                <div class="anim">
                                    <img src="https://s3.amazonaws.com/redpen-prod/red-pen-e37a8d47-6bc3-4828-eaa8-140b6857d23f.png" />
                                    <img src="https://s3.amazonaws.com/redpen-prod/red-pen-ab3019c2-e584-4f2a-e241-4ef26b3bff6a.png" />
                                    <img src="https://s3.amazonaws.com/redpen-prod/red-pen-ef2410cf-b0c7-45f5-c93c-255aba08ae9c.png" />
                                    <img src="https://s3.amazonaws.com/redpen-prod/red-pen-2772ff4c-47ab-430b-988e-bde2c88e42c1.png" />
                                    <img src="https://s3.amazonaws.com/redpen-prod/red-pen-6a64bf1d-5ae7-4a68-d37d-f575d49f30ff.png" />
                                    <img src="https://s3.amazonaws.com/redpen-prod/red-pen-a83f71c2-95a7-40d7-ce86-70eb2329fd8f.png" />
                                    <img src="https://s3.amazonaws.com/redpen-prod/red-pen-bf9170b3-13da-4b41-bd6c-ee17d8e96c5b.png" />
                                </div>
                            </div>
                        </div>
                    </section>


                    <section class="quote" v-if="!loading_quote">
                        <div class="quote-wrapper">
                            <div class="poster">

                                <progressive-img
                                    :src="actor_image_url_full" :blur="30"
                                    :placeholder="actor_image_url_thumb"
                                />

                                <!--<div class="progressive">-->
                                <!--<img class="preview" v-progressive="actor_image_url" :data-srcset="actor_image_url" :src="actor_image_preview_url" />-->
                                <!--</div>-->

                                <!--<img class="preview" v-progressive="actor_image_url" :data-srcset="actor_image_url" :src="actor_image_preview_url" />-->

                                <!--<img class="ui top aligned medium rounded image"-->
                                <!--v-bind:src="filmyQuotes.dialogue.star_image_urls.full">-->
                            </div>

                            <div class="content">

                                <img src="./assets/img/quote.svg" alt="Quote" class="quote_icon">
                                <h1 class="ibm-type-serif">{{filmyQuotes.dialogue.dialogue}}</h1>
                                <p class="text">-&nbsp;{{filmyQuotes.dialogue.star}}</p>

                                <div class="emoji">
                                    <ul class="reactions">
                                        <li v-for="emotion in filmyQuotes.dialogue.emotions">
                      <span class="reaction-emo">
                        <emoji set="apple" emoji="heart_eyes" :size="25" native
                               v-if="emotion.mood == 'heart_eyes'"></emoji>
                        <emoji set="apple" emoji="joy" :size="25" native v-if="emotion.mood == 'joy'"></emoji>
                        <emoji set="apple" emoji="flushed" :size="25" native v-if="emotion.mood == 'flushed'"></emoji>
                        <emoji set="apple" emoji="pensive" :size="25" native v-if="emotion.mood == 'pensive'"></emoji>
                        <emoji set="apple" emoji="rage" :size="25" native v-if="emotion.mood == 'rage'"></emoji>
                      </span>
                                            {{emotion.count}}
                                        </li>
                                    </ul>
                                    <div class="button" :class="{'loading':adding_reaction}" v-if="reaction_not_added">Add reaction
                                    </div>
                                    <div class="ui flowing popup top right transition hidden" v-if="reaction_not_added">
                                        <ul class="emojis-wrapper">
                                            <li class="emo">
                                                <emoji set="apple" emoji="heart_eyes" :size="35" native
                                                       v-on:click="add_reaction(filmyQuotes.dialogue.id,'heart_eyes')"></emoji>
                                            </li>
                                            <li class="emo">
                                                <emoji set="apple" emoji="joy" :size="35" native
                                                       v-on:click="add_reaction(filmyQuotes.dialogue.id,'joy')"></emoji>
                                            </li>
                                            <li class="emo">
                                                <emoji set="apple" emoji="flushed" :size="35" native
                                                       v-on:click="add_reaction(filmyQuotes.dialogue.id,'flushed')"></emoji>
                                            </li>
                                            <li class="emo">
                                                <emoji set="apple" emoji="pensive" :size="35" native
                                                       v-on:click="add_reaction(filmyQuotes.dialogue.id,'pensive')"></emoji>
                                            </li>
                                            <li class="emo">
                                                <emoji set="apple" emoji="rage" :size="35" native
                                                       v-on:click="add_reaction(filmyQuotes.dialogue.id,'rage')"></emoji>
                                            </li>
                                        </ul>
                                    </div>

                                </div>

                            </div>
                        </div>
                    </section>


                    <a href="javascript:void(0)" id="refresh" value="Refresh" v-on:click="get_quote()" v-shortkey="['space']" @shortkey="get_quote()" v-if="!loading_quote">
                        <svg class="icon"   version="1.1" id="Capa_1"  xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
     width="35px" height="35px" viewBox="0 0 322.447 322.447" style="enable-background:new 0 0 322.447 322.447;"
     xml:space="preserve">
        <g>
          <path  d="M321.832,230.327c-2.133-6.565-9.184-10.154-15.75-8.025l-16.254,5.281C299.785,206.991,305,184.347,305,161.224
            c0-84.089-68.41-152.5-152.5-152.5C68.411,8.724,0,77.135,0,161.224s68.411,152.5,152.5,152.5c6.903,0,12.5-5.597,12.5-12.5
            c0-6.902-5.597-12.5-12.5-12.5c-70.304,0-127.5-57.195-127.5-127.5c0-70.304,57.196-127.5,127.5-127.5
            c70.305,0,127.5,57.196,127.5,127.5c0,19.372-4.371,38.337-12.723,55.568l-5.553-17.096c-2.133-6.564-9.186-10.156-15.75-8.025
            c-6.566,2.134-10.16,9.186-8.027,15.751l14.74,45.368c1.715,5.283,6.615,8.642,11.885,8.642c1.279,0,2.582-0.198,3.865-0.614
            l45.369-14.738C320.371,243.946,323.965,236.895,321.832,230.327z"/>
        </g>
       </svg>
                    </a>


                    <div class="ui popup">
                        Refresh to get a new one!
                    </div>

                    <!--<picker @click="addEmoji"></picker>-->

                </div>
            </div>
        </div>

        <div class="quote-details" v-if="!loading_quote">

            <ul>
                <li class="movie-name">{{filmyQuotes.dialogue.movie_name}} <span
                    class="year">({{filmyQuotes.dialogue.movie_year}})</span>
                </li>
                <li class="tags">
             <span v-for="(tag,index) in filmyQuotes.dialogue.tags">
               {{ tag }}<span v-if="index<filmyQuotes.dialogue.tags.length-1">, </span>
             </span>
                </li>
            </ul>

        </div>


    </div>
</template>
<script>
    import {Picker} from 'emoji-mart-vue';
    import {Emoji} from 'emoji-mart-vue';
    import placeHolderUrl from './assets/img/placeholder.svg'

    const pickEmoji = [
        {
            name: 'pickemoji',
            short_names: ['pickemoji'],
            text: '',
            emoticons: [],
            keywords: ['pickemoji'],
            imageUrl: './assets/img/pickemoji.svg'
        },
    ];

    export default {


        components: {
            picker: Picker,
            emoji: Emoji
        },

        data() {
            return {

                filmyQuotes: {
                    "dialogue": {
                        "id": 0,
                        "dialogue": "",
                        "movie_name": "",
                        "star": "",
                        "movie_year": 20,
                        "tags": [],
                        "emotions": [],
                        "star_image_urls": {
                            "full": "",
                            "thumb": ""
                        }
                    }
                },
                actor_image_url: '',
                first_quote: true,
                loading_quote: false,
                actor_image_url_full: '',
                actor_image_url_thumb: '',
                reaction_not_added: true,
                adding_reaction: false,
                viewed_dialogues: "",
            }
        },
        mounted() {

        },

        computed: {},

        methods: {
            get_quote() {
                this.loading_quote = true;
                this.viewed_dialogues = this.$cookies.get("filmy_quotes_viewed_dialogues");
                let url = '/api/get-dialogues/?limit=1&remove-dialogues=';
                if(!this.viewed_dialogues){
                    url += '0'
                }else{
                    url += this.viewed_dialogues;
                }
                this.$http.get(url).then(response => {
                    this.loading_quote = false;
                    this.filmyQuotes = response.data;
                    if(this.filmyQuotes.dialogue.star_image_urls.full){
                        this.actor_image_url_full =  'https://image.tmdb.org/t/p/w500_and_h500_face/'+ this.filmyQuotes.dialogue.star_image_urls.full
                    }
                    else{
                        this.actor_image_url_full = placeHolderUrl
                    }

                    if(this.filmyQuotes.dialogue.star_image_urls.thumb){
                        this.actor_image_url_thumb =  'https://image.tmdb.org/t/p/w50_and_h50_face/'+ this.filmyQuotes.dialogue.star_image_urls.thumb
                    }
                    else{
                        this.actor_image_url_thumb = placeHolderUrl
                    }

                    setTimeout(function () {
                        $('.button')
                            .popup({
                                inline: true,
                                on: 'click',
                                variation: 'basic',
                                duration: 200,
                                onShow: function () {
                                    $(".button").addClass("active");
                                },
                                onHide: function () {
                                    $(".button").removeClass("active");
                                }
                            });

                    }, 10);
                    let new_dialogue = this.filmyQuotes.dialogue.id;
                    if(!this.viewed_dialogues){
                        this.viewed_dialogues = new_dialogue;
                    }else{
                        this.viewed_dialogues += ',' + new_dialogue;
                    }
                    this.$cookies.set("filmy_quotes_viewed_dialogues", this.viewed_dialogues, (60*60*24*7));
                }, response => {
                    this.loading_quote = false;
                });

            },

            onEnterClick: function() {
                alert('Enter was pressed');
            },



            add_reaction(id, mood) {
                this.adding_reaction = true;
                let data = {
                    'dialogue': id,
                    'mood': mood
                };
                this.$http.post('/api/add-emotion/', data).then(response => {
                    let emotions = this.filmyQuotes.dialogue.emotions;
                    let emotion_found = false;
                    let emotion_at = -1;
                    for (let i = 0; i < emotions.length; i++) {
                        if (emotions[i].mood === mood) {
                            emotion_found = true;
                            emotion_at = i;
                            break
                        }
                    }
                    if (emotion_found) {
                        emotions[emotion_at].count = emotions[emotion_at].count + 1;
                    } else {
                        emotions.push({
                            mood: mood,
                            count: 1
                        })
                    }
                    this.filmyQuotes.dialogue.emotions = emotions;
                    this.reaction_not_added = false;
                    this.adding_reaction = false;
                }, response => {
                    this.adding_reaction = false;
                });
            },

            set_fontsize() {
                var $quote = $(".quote h1");
                var $numWords = $quote.text().split().length;

                if (($numWords >= 1) && ($numWords < 10)) {
                    $quote.css("font-size", "36px");
                }
                else if (($numWords >= 10) && ($numWords < 20)) {
                    $quote.css("font-size", "32px");
                }
                else if (($numWords >= 20) && ($numWords < 30)) {
                    $quote.css("font-size", "32px");
                }
                else if (($numWords >= 30) && ($numWords < 40)) {
                    $quote.css("font-size", "33px");
                }
                else if (($numWords >= 30) && ($numWords < 80)) {
                    $quote.css("font-size", "26px");
                }
                else {
                    $quote.css("font-size", "32px");
                }
            },


        },


        updated(){
            setTimeout(function () {
//        $('#refresh')
//          .popup({
//            position: 'top center',
//            delay: {
//              show: 30,
//              hide: 30
//            }
//          })
//        ;
            }, 15);
        },
        mounted() {
            this.get_quote();
        }
    }

</script>



<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">
        @import './assets/css/semantic.min.css';
        @import './assets/css/animate.css';
        @import '../node_modules/inter-ui/inter-ui.css';
        @import '../node_modules/@ibm/type/css/ibm-type.min.css';
        @import './assets/css/main.css';

</style>
