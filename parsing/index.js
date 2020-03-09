import cherio from 'cherio';
import chalk from 'chalk';
import {arrayFromLength} from './helpers/common';
import {getPageContent} from './puppeteer';
var fs = require("fs");

import { slugify } from 'transliteration';

const page=3;
const phoneItem=[];
const SITE='https://www.mechta.kz/section/apple-eql/?PAGEN_2=';
(async function main(){
    try{
        for (const page of arrayFromLength(1)) {
            const url=`${SITE}${page}`;
            const pageContent = await getPageContent(url);
            const   $ = cherio.load(pageContent);
            
    
            $('.j_product_link').each((i,header)=>{
                const title=$(header).text();
                if (title !== "") {
                    phoneItem.push({
                        title
                        
                    });
                } 

                

            });
            $('.aa_std_bigprice').each((i,header)=>{
                const price=$(header).text();
                phoneItem.push({
                    price
                });
            });
            console.log(phoneItem);
            

            
        }
        // phoneItem.forEach(element => {
        //     console.log(element);
        // });
    }
    catch(err){
        console.log(chalk.red('An error has occured \n'));
        console.log(err);
    }

})();

