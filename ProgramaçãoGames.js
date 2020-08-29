//CLASSE PRELOADER.js    
//FUNCTION PRELOADER
//carregando imagem do fundo
this.load.image('background','images/backGroundGame800x600.png');
//carregando imagem da nuvem
this.load.image('cloud','images/Cloud.png');
//CLASSE GAME.js
//FUNCTION CREATE
//Adicionando nuvens a camada cloudLayer.this.cloudOne=this.add.sprite(0,0,'cloudOne');
this.cloudLayer.add(this.cloudOne);
//FUNCTION UPDATE
//movimentando a nuvem
this.cloudOne.x+=this.directionCloud;
if(this.directionCloud>0){
if(this.cloudOne.x-=this.game.width;
} else if(this.cloudOne.x<-163){
this.cloudOne.x += this.game.width;
}
}   
